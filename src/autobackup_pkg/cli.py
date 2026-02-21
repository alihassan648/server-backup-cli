import argparse
import sys

from .commands.backup import backup_command
from .commands.restore import restore_command
from .commands.list_backups import list_command
from .logger import get_logger

logger = get_logger()


def main():
    parser = argparse.ArgumentParser()

    sub = parser.add_subparsers(dest="command")

    # Backup
    backup_parser = sub.add_parser("backup")
    backup_parser.add_argument("--source", required=True)
    backup_parser.add_argument("--dest", required=True)
    backup_parser.add_argument("--verify", action="store_true")

    # Restore
    restore_parser = sub.add_parser("restore")
    restore_parser.add_argument("--file", required=True)
    restore_parser.add_argument("--dest", required=True)

    # List
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--dest", required=True)

    args = parser.parse_args()

    try:
        if args.command == "backup":
            backup_command(args)

        elif args.command == "restore":
            restore_command(args)

        elif args.command == "list":
            list_command(args)

    except Exception as e:
        logger.exception(f"Error running {args.command}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()