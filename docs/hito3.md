# Hito 3 – Microservice Design

---

## 1. Milestone Goal

- Design a microservice exposing a REST API
- Separate API layer and business logic using dependency injection
- Add API and logic tests
- Add logging for API activity
- Provide a build/task file so CI runs the same commands

---

## 2. Technical Choices (Justification)

- **Framework:** FastAPI (simple, fast, DI built-in, automatic docs)
- **Test Runner:** pytest (widely used, easy, already used in Hito 2)
- **Assertions:** Python `assert` (Simple and native)
- **Task Runner:** Makefile ( Standard DevOps practice, used by CI)
- **Logging:** Python `logging` + FastAPI middleware, Unified structured logs

---

## 3. API Design (Routes)

- `POST /api/bars` → create a bar (`name`, `city`) → returns `201` with `{id,name,city}`
- `GET  /api/bars` → list all bars → `{ "items": [ ... ] }`

- API file: `app/api/routes.py`
- Logic file: `app/services/logic.py`
- Dependency injection for repository

---

## 4. Architecture / Project Structure
TapasMap-Granada/
├── app/
│ ├── main.py
│ ├── api/
│ │ └── routes.py
│ ├── services/
│ │ └── logic.py
│ └── core/
│ └── logging_config.py
├── tests/
│ ├── test_logic.py
│ └── test_api.py
├── Makefile
├── requirements.txt
└── docs/
└── hito3.md

---

## 5. Logging

- Middleware logs request start/end and status code
- Central configuration in `app/core/logging_config.py`
- Helps debugging and observability

## 6. Tests

- Logic: `tests/test_logic.py`
- API: `tests/test_api.py` (uses `with TestClient(app)` to ensure lifespan)
- Run locally: `pytest`
- Run in CI: `make ci`

---

## 7. Build & Automation

Makefile commands:

- `make install` → install dependencies  
- `make test` → run tests  
- `make ci` → install + test (used in GitHub Actions)

---

## 8.Evidence
- CI run passed (green check)
- Screenshot: ![Test Result Screenshot](Screenshot%20CI%20run%20passsed.png)

---

## 9. Conclusion

- Microservice created with FastAPI
- API separate from business logic
- Logging integrated
- Tests cover logic and API
- CI runs tests automatically via Makefile
- Architecture follows microservice + dependency-injection design


