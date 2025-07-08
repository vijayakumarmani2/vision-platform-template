import yaml
import os
from src.utils.custom_log import log_event  
from datetime import datetime

def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def process_inputs(input_path, output_path):
    log_event(f"Scanning input folder: {input_path}")
    if not os.path.exists(input_path):
        log_event(f"Input path does not exist: {input_path}")
        return

    files = os.listdir(input_path)
    log_event(f"Found {len(files)} files to process.")

    os.makedirs(output_path, exist_ok=True)
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_filename = f"processed_{timestamp}_{file}"
            dest_path = os.path.join(output_path, new_filename)
            log_event(f"Simulating image processing: {file} -> {dest_path}")
            with open(dest_path, 'w') as f:
                f.write("dummy image content")

if __name__ == "__main__":
    config = load_config()
    log_event("Configuration loaded successfully.")
    process_inputs(config['input_path'], config['output_path'])