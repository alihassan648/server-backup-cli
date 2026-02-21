from pathlib import Path
import tarfile
import datetime

from ..logger import get_logger

logger = get_logger()


def backup_command(args):

    source = Path(args.source).expanduser().resolve()
    dest = Path(args.dest).expanduser().resolve()

    dest.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = f"backup_{source.name}_{timestamp}.tar.gz"
    backup_path = dest / backup_name

    logger.info(f"Verifying {backup_path}")

    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(source, arcname=source.name)

    logger.info(f"Backup completed successfully: {backup_path}")