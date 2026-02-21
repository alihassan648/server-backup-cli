import os
import shutil

def copy_file(src, dest):
    shutil.copy2(src, dest)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
