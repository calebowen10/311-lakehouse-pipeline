from pathlib import Path
import json

STATE_PATH = Path("state/watermark.json")


def get_last_watermark():
    if not STATE_PATH.exists():
        return None

    with open(STATE_PATH, "r") as f:
        data = json.load(f)

    return data.get("last_created_date")


def save_watermark(ts):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(STATE_PATH, "w") as f:
        json.dump({"last_created_date": ts}, f)
