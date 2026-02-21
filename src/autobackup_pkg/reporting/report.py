import json

def save_report(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
