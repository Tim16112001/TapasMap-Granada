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

Example mapping:
```yaml
ports:
  - "8000:8000"   # API
  - "8080:8080"   # Adminer
volumes:
  - db_data:/var/lib/postgresql/data

All containers share a single network for communication.
Configuration-as-code ensures identical startup on any host.

---

## 4. Continous Integration




