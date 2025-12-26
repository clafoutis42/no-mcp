import os

from app.logging import init_logging

worker_class = "uvicorn.workers.UvicornWorker"
workers = os.environ.get("GUNICORN_WORKERS", 3)
bind = "0.0.0.0:8000"

logger_class = "app.logging.gunicorn.GunicornLogger"

init_logging()
