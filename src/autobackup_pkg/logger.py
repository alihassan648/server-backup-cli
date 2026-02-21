import logging
from .logging_config import setup_logging

def get_logger(name: str = "autobackup"):
    setup_logging()
    return logging.getLogger(name)