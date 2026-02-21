import logging
import os

LOG_FILE = "autobackup.log"

def setup_logging():
    if logging.getLogger().handlers:
        return

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/autobackup.log"),
            logging.StreamHandler()
        ]
    )