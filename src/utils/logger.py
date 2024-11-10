import logging
import sys
from logging import StreamHandler, Formatter, Logger

log_level = logging.INFO


def get_stream_handler() -> StreamHandler:
    _log_format: str = "%(asctime)s - [%(levelname)s] - %(message)s"
    stream_handler: StreamHandler = StreamHandler(sys.stdout)
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(Formatter(_log_format))
    return stream_handler


def get_logger(name: str) -> Logger:
    logger: Logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(log_level)
        logger.addHandler(get_stream_handler())

    return logger
