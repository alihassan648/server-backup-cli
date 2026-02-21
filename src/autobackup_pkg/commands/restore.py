import tarfile
from pathlib import Path
from ..logger import get_logger

logger = get_logger()


def restore_command(args):

    file_path = Path(args.file).expanduser().resolve()
    dest = Path(args.dest).expanduser().resolve()

    dest.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(dest)

    logger.info(f"Restore completed successfully: {file_path}")