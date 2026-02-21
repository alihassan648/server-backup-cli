import json
import os

def load_config(file_path="config.json"):
    if not os.path.exists(file_path):
        return {}
    with open(file_path) as f:
        return json.load(f)
