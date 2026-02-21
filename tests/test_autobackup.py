import os
import pytest
from autobackup_pkg.commands.backup import backup_command
from autobackup_pkg.commands.restore import restore_command

def test_backup_restore_list(tmp_path):

    # Setup folders
    test_src = tmp_path / "test_data"
    test_dest = tmp_path / "backups"
    restore_dest = tmp_path / "restored"

    test_src.mkdir()
    test_dest.mkdir()
    restore_dest.mkdir()

    # Create test files
    (test_src / "file1.txt").write_text("Hello")
    (test_src / "file2.txt").write_text("World")

    # 1️⃣ Backup
    backup_command(["--source", str(test_src), "--dest", str(test_dest), "--verify"])

    backup_files = list(test_dest.glob("*.tar.gz"))
    assert len(backup_files) == 1

    # 2️⃣ Restore
    restore_command(["--file", str(backup_files[0]), "--dest", str(restore_dest)])

    # 3️⃣ Check restored structure
    restored_subdir = restore_dest / "test_data"
    assert restored_subdir.exists()

    restored_files = os.listdir(restored_subdir)
    original_files = os.listdir(test_src)

    assert set(restored_files) == set(original_files)