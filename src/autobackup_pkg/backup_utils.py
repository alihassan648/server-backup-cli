# autobackup_pkg/backup_utils.py

import os
import tarfile
import hashlib
from datetime import datetime
from autobackup_pkg.core.logger import logger

def create_backup(source_dir: str, dest_dir: str) -> str:
    """
    Create a tar.gz backup of the source directory in the destination directory.

    Args:
        source_dir (str): Directory to backup.
        dest_dir (str): Destination directory to store backup.

    Returns:
        str: Path to the created backup file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    source_name = os.path.basename(os.path.normpath(source_dir))
    backup_filename = f"backup_{source_name}_{timestamp}.tar.gz"
    backup_path = os.path.join(dest_dir, backup_filename)

    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(source_dir, arcname=source_name)
        logger.info(f"Backup created at {backup_path}")
        return backup_path
    except Exception as e:
        logger.error(f"Failed to create backup: {e}")
        raise

def verify_backup(backup_path: str) -> bool:
    """
    Verify the integrity of the backup by checking if it can be opened.

    Args:
        backup_path (str): Path to the backup file.

    Returns:
        bool: True if verification succeeds, False otherwise.
    """
    if not os.path.exists(backup_path):
        logger.error(f"Backup file does not exist: {backup_path}")
        return False

    try:
        with tarfile.open(backup_path, "r:gz") as tar:
            bad_file = tar.testzip()  # Returns None if no error
            if bad_file:
                logger.error(f"Corrupted file found in backup: {bad_file}")
                return False
        logger.info(f"Backup verification successful: {backup_path}")
        return True
    except Exception as e:
        logger.error(f"Backup verification failed: {e}")
        return False

def hash_file(file_path: str) -> str:
    """
    Generate SHA256 hash of a file. Can be used for backup integrity checking.

    Args:
        file_path (str): File path to hash.

    Returns:
        str: Hex digest of the file.
    """
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()