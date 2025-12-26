import os

from app.logging import init_logging
from app.presentation.mcp.container import Container
from app.settings import Settings

worker_class = "uvicorn.workers.UvicornWorker"
workers = os.environ.get("GUNICORN_WORKERS", 3)
bind = "0.0.0.0:8000"

logger_class = "app.logging.gunicorn.GunicornLogger"

container = Container()
container.config.from_pydantic(Settings())
container.wire(packages=["app.presentation.mcp"])

init_logging()
