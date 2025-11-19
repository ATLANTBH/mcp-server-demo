from datetime import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
PROJECT_ROOT = os.path.dirname(BASE_DIR)               
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

def post_report(title: str, content: str):
    """Simulate saving a report to disk inside /reports directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = title.replace(" ", "_")
    filename = f"{timestamp}_{safe_title}.json"
    path = os.path.join(REPORTS_DIR, filename)

    report_data = {
        "title": title,
        "content": content,
        "timestamp": timestamp
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    return {"status": "success", "path": path}
