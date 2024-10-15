import logging
from logging import StreamHandler, INFO, Formatter, Logger


def get_stream_handler() -> StreamHandler:
    """
    This function creates a StreamHandler for the logger.
    It sets the logging level to INFO and formats the log messages.

    :return: A StreamHandler object for output to the console.
    :rtype: StreamHandler
    """

    _log_format: str = "%(asctime)s - [%(levelname)s] - %(message)s"
    stream_handler: StreamHandler = StreamHandler()
    stream_handler.setLevel(INFO)
    stream_handler.setFormatter(Formatter(_log_format))
    return stream_handler


def get_logger(name: str) -> Logger:
    """
    This function creates a logger with the given name.
    It sets the logging level to INFO and adds the StreamHandler to the logger.

    :param name: name of the logger.
    :type name: str
    :return: logger object.

    :rtype: Logger
    """

    logger: Logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_stream_handler())
    return logger