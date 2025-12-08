# Hito 5 – Cloud Deployment on a PaaS

---

## 1. Milestone Goal

- Deploy the TapasMap API to a public cloud (PaaS)  
- Automate deployment from the GitHub repository  
- Add observability (logs, health check, metrics)  
- Run basic performance tests on the deployed application  
- Document the full deployment and monitoring setup  

---

## 2. PaaS Selection and Justification

For this milestone I selected **Render.com** as the PaaS provider.

**Criteria:**

- **European region support:** Render offers an EU region (e.g. Frankfurt), which satisfies the legal requirement to deploy in Europe.  
- **GitHub integration:** Render connects directly to a GitHub repository and triggers deployments automatically on every push to `main`.  
- **Docker support:** My project already uses a `Dockerfile` from Hito 4, so using a Docker-based PaaS avoids rewriting the build process.  
- **Free tier:** Render provides a free tier sufficient for a small FastAPI microservice.  

Alternative options considered were **Railway.app** and **Heroku**, but Render was chosen because of the Docker support and EU region availability.

---

## 3. Deployment Configuration (Tools and Steps)

### 3.1 Dockerfile

The application is containerised using the `Dockerfile` created in Hito 4:

- Base image: `python:3.12-slim`  
- Install dependencies from `requirements.txt`  
- Copy application code into `/app`  
- Expose port `8000`  
- Start command:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000

This is the same build process used locally and in CI, so the runtime environment is consistent across local, CI and cloud.

### 3.2 Render service configuration

On Render, I created a Web Service with the following configuration:

- **Repository:** Tim16112001/TapasMap-Granada.
- **Branch:** main.
- **Runtime:** Docker (Render uses the Dockerfile at the repo root)
- **Region:** EU (Frankfurt)
- **Port:** 8000 (taken from the Dockerfile / Uvicorn command)
Deployment URL (public):
- **URL:** https://tapasmap-granada.onrender.com

---

## 4. Automatic Deployment from GitHub

Render is linked directly to the GitHub repository. Every time I push to the main branch:

1. Render pulls the latest commit from GitHub.
2. Render builds a new Docker image using the Dockerfile.
3. The new container is started and the previous one is replaced.

This provides an automated CI/CD style workflow based only on git push.
No manual build or upload is needed after the initial configuration.

---

## 5. Observability and Monitoring

### 5.1 Logging

Application logging is configured using:

- app/core/logging_config.py – sets up the logging configuration.
- A middleware in app/main.py:
  @app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("request start %s %s", request.method, request.url.path)
    response = await call_next(request)
    logger.info(
        "request end %s %s status=%s",
        request.method,
        request.url.path,
        response.status_code,
    )
    return response
  
This logs every request with method, path and status code.
In Render, these logs are visible in the Logs tab in real time.

### 5.2 Health Check Endpoint

To check that the application is alive, a simple health route is exposed in app/main.py:
@app.get("/health")
def health_check():
    return {"status": "ok"}
    
This endpoint is publicly accessible at: 
- https://tapasmap-granada.onrender.com/health


### 5.3 API Documentation (Swagger)

FastAPI automatically generates interactive API documentation:
- https://tapasmap-granada.onrender.com/docs

This allows checking the available endpoints (/api/bars) and testing them interactively.

---

## 6. Functional Tests on the Deployed Application

To verify that the API works correctly in the cloud, I executed the following requests from my local machine:

### 6.1 Create a bar in the cloud

Invoke-RestMethod `
  -Method POST `
  -Uri https://tapasmap-granada.onrender.com/api/bars `
  -ContentType "application/json" `
  -Body '{"name":"Cloud Bar","city":"Granada"}'

### 6.2 List all bars in the cloud

Invoke-RestMethod -Method GET -Uri https://tapasmap-granada.onrender.com/api/bars

The response contained the created bar with status codes 201 (POST) and 200 (GET), confirming that the backend logic works correctly in the PaaS environment.

---

## 7. Performance and Load Tests

To perform a simple performance test, I sent multiple POST requests in a short time frame:

1..20 | ForEach-Object {
  Invoke-RestMethod `
    -Method POST `
    -Uri https://tapasmap-granada.onrender.com/api/bars `
    -ContentType "application/json" `
    -Body '{"name":"Cloud Load Test","city":"Granada"}'
}

Then I checked the number of stored bars:

Invoke-RestMethod -Method GET -Uri https://tapasmap-granada.onrender.com/api/bars

Observations:
- All POST requests completed successfully without errors.
- The API remained responsive during the test.
- Latency per request was well below one second from the client perspective.
- Render did not report any errors or restarts in the Logs tab.

---

## 8. Conclusions

- The TapasMap-Granada API is successfully deployed on a PaaS (Render) in an EU region.
- Deployment is fully automated: a simple git push to main triggers a new build and deployment.
- Observability is implemented using structured logs, a health endpoint and the Render dashboard.
- Basic performance tests confirm that the API behaves correctly under a small concurrent load.

This milestone completes the end-to-end pipeline from local development and CI, through containerisation, to automated cloud deployment and monitoring.




