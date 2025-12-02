import logging
from fastapi import FastAPI, Request

from app.api.routes import router
from app.core.logging_config import setup_logging
from app.services.repository import InMemoryBarRepository

# Configure logging once at import time
setup_logging()
logger = logging.getLogger("tapasmap.api")


def create_app() -> FastAPI:
    app = FastAPI(title="TapasMap-Granada API")

    # Initialize in-memory repository (single source of truth)
    @app.on_event("startup")
    def startup_event() -> None:
        app.state.repo = InMemoryBarRepository()

    # Simple logging middleware for observability
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

    # Include all API routes (they already have prefix="/api")
    app.include_router(router)

    # Health route for cloud monitoring
    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app


# This is the ASGI app object Uvicorn/Render and tests import
app = create_app()
