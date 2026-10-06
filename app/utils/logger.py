from __future__ import annotations

import logging


def configure_logging(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("trading_agent")
    logger.setLevel(level.upper())

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(handler)

    return logger
