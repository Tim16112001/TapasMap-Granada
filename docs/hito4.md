# Hito 4 – Service Composition with Docker and Compose

---

## 1. Milestone Goal

- Containerize the TapasMap API using Docker  
- Create a reproducible multi-service environment with Docker Compose  
- Include at least one data-storage container  
- Configure automated image publishing to GitHub Container Registry (GHCR)  
- Verify functionality through CI/CD integration tests  
- Document and visualize the whole setup

---

## 2. Technical Justification

**Framework:** FastAPI – lightweight, asynchronous, and ideal for microservices  
**Container base image:** `python:3.12-slim` – small size and official Python build  
**Orchestration:** Docker Compose – easy local testing and reproducible multi-service setup  
**CI/CD:** GitHub Actions – automates both image builds and Compose tests  
**Registry:** GHCR (GitHub Container Registry) – directly linked to the repository  
**Logging:** Python `logging` + FastAPI middleware  

---

## 3. Docker and Service Design

### 3.1 Dockerfile (for the API)
- Starts from `python:3.12-slim`  
- Installs dependencies from `requirements.txt`  
- Copies source code into `/app`  
- Runs the API with Uvicorn (`CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]`)

### 3.2 Docker Compose (`compose.yaml`)
Three-service cluster:
1. **api** – FastAPI microservice (`tapasmap-api`)  
2. **db** – PostgreSQL container for persistent data  
3. **adminer** – simple database admin UI  

Example Mapping:
ports:
  - "8000:8000"   # API
  - "8080:8080"   # Adminer
volumes:
  - db_data:/var/lib/postgresql/data

All containers share a single network for communication.
Configuration-as-code ensures identical startup on any host.

---

## 4. Continous Integration

Two automated workflows run on every push:
1. **publish-image.yml** – builds and pushes the Docker image to GHCR.
2. **compose-test.yml** – launches the full Compose cluster and runs test requests.

Both appear as green checkmarks in the GitHub Actions tab.

---

## 5. GHCR Image Publication

- Repository: ghcr.io/tim16112001/tapasmap-api:latest
- Automatically built and published by GitHub Actions
- Package is public and linked to the main repository
- Screenshot - GHCR package
  ![GHCR Package](../ghcr_package.png)

---

## 6. Verification and Testing

After running: `docker compose up -d`

The API can be tested via: 
`Invoke-RestMethod -Method POST -Uri http://localhost:8000/api/bars -ContentType "application/json" -Body '{"name":"Bar Compose","city":"Granada"}'
Invoke-RestMethod -Method GET  -Uri http://localhost:8000/api/bars`

Expected result:
id name        city
-- ----        ----
1  Bar Compose Granada

---

## 7. Documentation and Evidence

- All configuration files: Dockerfile, .dockerignore, compose.yaml
- CI configuration: .github/workflows/publish-image.yml,.github/workflows/compose-test.yml
- Screenshots embedded directly (visible above)
- Source repository linked from the GHCR package

---

## 8. Conclusions

This milestone completes the containerization stage:
- The TapasMap API can now be built, deployed, and tested reproducibly.
- The environment is portable and ready for future deployment to cloud platforms.
  


