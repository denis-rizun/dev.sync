import logging
import sys

from colorlog import ColoredFormatter

from backend.core.config import config


class Logger:
    FMT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    DATEFMT = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def setup_logger(cls, name: str = __name__) -> logging.Logger:
        cls._setup_other_loggers()

        logger = logging.getLogger(name)
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.setLevel(logging.INFO)

        if not config.ENABLE_LOGGER:
            simple_handler = logging.StreamHandler(sys.stdout)
            simple_handler.setLevel(logging.INFO)
            simple_handler.setFormatter(logging.Formatter("%(message)s"))
            logger.addHandler(simple_handler)
            return logger

        if config.ENABLE_COLORED_LOGS:
            try:
                formatter = ColoredFormatter(
                    fmt=f"%(log_color)s{cls.FMT}",
                    datefmt=cls.DATEFMT,
                    force_color=True,
                    log_colors={
                        "DEBUG": "cyan",
                        "INFO": "green",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "bold_red",
                    },
                )
            except ImportError:
                formatter = logging.Formatter(
                    fmt=cls.FMT,
                    datefmt=cls.DATEFMT,
                )
        else:
            formatter = logging.Formatter(
                fmt=cls.FMT,
                datefmt=cls.DATEFMT,
            )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    @classmethod
    def _setup_other_loggers(cls) -> None:
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
        logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)
        logging.getLogger("alembic").setLevel(logging.INFO)
        logging.getLogger("aiogram").setLevel(logging.ERROR)
