# TapasMap-Granada

Project: TapasMap – Community Tapas & Bar Tracker for Granada  
Student: Tim Severein  
Email: tim.severein@stud.uni-due.de 
Course: Cloud Computing: Fundamentos e Infraestructuras - 2526 (COMÚN)  

---

## Description

TapasMap-Granada is a web application that allows users to discover, rate, and share recommendations for tapas bars in Granada.  

The goal of this project is to develop a simple application that can later be deployed in the cloud, focusing on server logic and data management.

---

## Hito 1 – Practice Repository

For Hito 1, the following tasks have been completed:

- Installed and configured Git and GitHub
- Created an SSH key and uploaded it to GitHub
- Set up GitHub profile (name, location, university, profile picture, 2FA)
- Created the repository `TapasMap-Granada`
- Created folder structure for documentation (`docs/`) and screenshots (`docs/images/`)

Full Hito 1 documentation is available in [`docs/hito1.md`](docs/hito1.md).

---

## Hito 2 – Continuous Integration

For Hito 2, the following tasks have been completed:

- Set up virtual environment (`venv`) for Python project
- Installed test framework `pytest` and configured dependencies in `requirements.txt`
- Created a test file `tests/test_tracker.py` to verify the functionality of `add_bar` in `tapas.py`
- Configured GitHub Actions workflow (`.github/workflows/python-tests.yml`) to automatically run tests on every push
- Ran tests locally to ensure they pass successfully
- Verified that tests run automatically in GitHub Actions (CI), as shown by the green check mark
- Full Hito 2 documentation is available in [`docs/hito2.md`](docs/hito2.md)

---

## Hito 3 – Microservice

For Hito 3, the following tasks have been completed:

- Added FastAPI microservice with REST endpoints
- Separated API and business logic via dependency injection
- Implemented logging middleware
- Added API + logic tests with pytest
- Introduced Makefile for unified local and CI execution
- CI workflow now runs `make ci`
- See full documentation: [`docs/hito3.md`](docs/hito3.md)

---

## Hito 4 – Service Composition (Docker & GHCR)

For Hito 4, the following tasks have been completed:

- Dockerfile for the FastAPI microservice (`python:3.12-slim`)
- Multi-container setup via `compose.yaml` (API + PostgreSQL + Adminer)
- Automatic image publishing to GHCR
- CI workflows: build & push + compose cluster test
- See full documentation: [docs/hito4.md](docs/hito4.md)

## License

This project is licensed under the [MIT License](LICENSE).
