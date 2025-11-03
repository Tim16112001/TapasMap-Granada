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
- **Test Runner:** pytest (widely used, minimal setup)
- **Assertions:** Python `assert`
- **Task Runner:** Makefile (`make ci` used in CI)
- **Logging:** Python `logging` + middleware for request start/end and status

---

## 3. API Design (Routes)

- `POST /api/bars` → create a bar (`name`, `city`) → returns `201` with `{id,name,city}`
- `GET  /api/bars` → list all bars → `{ "items": [ ... ] }`

Business logic in `app/services/logic.py`, repository via DI (`InMemoryBarRepository`).

---

## 4. Logging

- Central config in `app/core/logging_config.py`
- Request middleware logs method, path, status

---

## 5. Tests

- Logic: `tests/test_logic.py`
- API: `tests/test_api.py` (uses `with TestClient(app)` to ensure lifespan)
- Run locally: `pytest`
- Run in CI: `make ci`

---

## 6. Build/Tasks

- `Makefile` targets: `install`, `test`, `run`, `ci`

---

## 7.Evidence
- CI run passed (green check)
- Screenshot: ![Test Result Screenshot](docs/Screenshot%20CI%20run%20passsed.png)


