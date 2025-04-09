import os
import logging


import tomllib

default_path = "logging_config.toml"

if os.path.exists(default_path):
    with open("logging_config.toml", "rb") as f:
        config = tomllib.load(f)
        logging.config.dictConfig(config)

log_level = os.getenv("LOG_LEVEL", "ERROR").upper()
logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, log_level, logging.INFO))
