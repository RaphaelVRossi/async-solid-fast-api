import os
import logging


import tomllib


def _get_logger(config_path="logging_config.toml"):
    if os.path.exists(config_path):
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
            logging.config.dictConfig(config)

    log_level = os.getenv("LOG_LEVEL", "ERROR").upper()
    _logger = logging.getLogger(__name__)
    _logger.setLevel(getattr(logging, log_level, logging.INFO))

    return _logger


logger = _get_logger()
