from datetime import datetime
import json
import os
import tempfile

REPORTS_DIR = os.path.join(tempfile.gettempdir(), "mock_company_reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def post_report(title: str, content: str):
    """Simulate saving a report to disk."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{REPORTS_DIR}/{timestamp}_{title.replace(' ', '_')}.json"
    
    report_data = {
        "title": title,
        "content": content,
        "timestamp": timestamp
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)
    
    return {"status": "success", "path": filename}
