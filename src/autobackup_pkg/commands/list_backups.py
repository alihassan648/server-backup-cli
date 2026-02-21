from pathlib import Path
from ..logger import get_logger

logger = get_logger()


def list_command(args):

    dest = Path(args.dest).expanduser().resolve()

    if not dest.exists():
        print("Backups: []")
        return

    backups = sorted([f.name for f in dest.glob("*.tar.gz")])

    print(f"Backups: {backups}")