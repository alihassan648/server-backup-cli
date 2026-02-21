from pathlib import Path


LOCK_FILE = Path(".autobackup.lock")


def acquire_lock() -> Path:
    if LOCK_FILE.exists():
        raise RuntimeError("Another backup process is already running.")

    LOCK_FILE.write_text("locked")
    return LOCK_FILE


def release_lock(lock_file: Path) -> None:
    if lock_file.exists():
        lock_file.unlink()