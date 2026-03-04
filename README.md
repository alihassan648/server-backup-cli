

# Server Backup CLI

## Overview

**Server Backup CLI** is a production-ready Python command-line automation tool designed for server file backup, restoration, and backup management.

The project follows DevOps-style architecture principles and is suitable for portfolio showcase and freelance automation tasks.

This project is developed by **alihassan648** as part of a Python DevOps automation portfolio.

---

## Features

- Automated file backup using compressed archive format (.tar.gz)
- Restore backup functionality
- List available backups
- Backup verification mode
- Structured logging system
- Production-style project structure
- Editable pip installation support
- CLI-based automation interface

---

## Project Architecture

The project is structured using **modern Python packaging practices**:

src/
└── autobackup_pkg/
├── cli.py
├── backup.py
├── restore.py
├── list_backups.py
├── logger.py
├── core/
├── reporting/
└── utils.py

---

## Installation

### Clone Repository

```bash
git clone https://github.com/alihassan648/server-backup-cli.git
cd server-backup-cli


⸻

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate


⸻

Install Package

pip install -e .


⸻

Usage

Backup Files

autobackup backup --source test_data --dest backups --verify

Options:
	•	--source → Source directory
	•	--dest → Backup storage directory
	•	--verify → Enable integrity verification

⸻

List Available Backups

autobackup list --dest backups


⸻

Restore Backup

autobackup restore --file backups/backup_file.tar.gz --dest restored_data


⸻

Logging System

The project uses centralized logging configuration located in:

autobackup_pkg/logger.py

Logs are stored inside:

logs/autobackup.log


⸻

Testing

Run unit tests using:

pytest -v


⸻

Requirements
	•	Python 3.10+
	•	setuptools
	•	wheel
	•	pytest (development only)

⸻

Future Improvements
	•	GitHub Actions CI pipeline
	•	Backup scheduling system
	•	Encryption support
	•	Remote server backup integration
	•	Dashboard monitoring support

⸻

License

MIT License

⸻

Author

alihassan648

GitHub: https://github.com/alihassan648

---







