import logging
import sys

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(name)s %(message)s'
    )
    handler.setFormatter(fmt)

    # Doppelte Handler vermeiden
    if not logger.handlers:
        logger.addHandler(handler)

    # Uvicorn/FastAPI-Logger auf INFO
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)
