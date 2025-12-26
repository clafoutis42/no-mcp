from gunicorn.glogging import Logger

from .intercept_handler import InterceptHandler


class GunicornLogger(Logger):
    def setup(self, cfg):
        """Configure Gunicorn application logging configuration."""
        super().setup(cfg)
        self.access_log.handlers = [InterceptHandler()]
        self.error_log.handlers = [InterceptHandler()]
