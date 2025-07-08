import json
from datetime import datetime

def log_event(message: str):
    log = {
        "timestamp": datetime.now().isoformat(),
        "event": message
    }
    print(json.dumps(log))