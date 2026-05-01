import json
import os
from datetime import date

LOG_FILE = 'tracking/weight_log.json'

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            return json.load(f)
    return []

def save_log(log):
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

def add_entry(weight_kg):
    log = load_log()
    log.append({'date': str(date.today()), 'weight': weight_kg})
    save_log(log)
    return log

def get_trend(log):
    """Simple linear trend from last 7 entries."""
    if len(log) < 2:
        return None
    recent = log[-7:]
    weights = [e['weight'] for e in recent]
    avg_change = (weights[-1] - weights[0]) / len(weights)
    return round(avg_change, 2)