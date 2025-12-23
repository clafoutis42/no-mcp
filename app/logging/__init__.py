import logging
import sys

from loguru import logger

from app.settings import settings as config

from .intercept_handler import InterceptHandler

__all__ = ["init_logging"]


def _init_intercept():
    # change handler of default uvicorn logger
    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    logging.getLogger("uvicorn.access").handlers = [intercept_handler]
    logging.basicConfig(handlers=[intercept_handler], level=0, force=True)


def _init_dev_handler():
    logger.add(
        sys.stdout,
        level=config.LOG_LEVEL.upper(),
        backtrace=True,
        diagnose=True,
    )


def _record_patcher(event_dict):
    event_dict["extra"]["environment"] = config.ENVIRONMENT
    event_dict["extra"]["service"] = config.SERVICE

    return event_dict


def _init_prod_handler():
    logger.add(
        sys.stdout,
        format="{message}",
        serialize=True,
        level=config.LOG_LEVEL.upper(),
    )
    logger.configure(patcher=_record_patcher)


def init_logging():
    """
    Initiates loguru.
    """
    logger.remove()

    match config.ENVIRONMENT:
        case "staging" | "production":
            _init_prod_handler()
        case _:
            _init_dev_handler()

    _init_intercept()
