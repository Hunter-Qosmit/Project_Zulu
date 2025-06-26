from datetime import datetime
from collections import deque

MAX_HISTORY = 10

metrics_data = {
    "total_requests": 0,
    "successful_requests": 0,
    "failed_requests": 0,
    "errors_by_type": {},  # e.g., {"http_error": 2, "timeout": 1}
    "chaos_events": [],    # recent chaos events (type + timestamp)
    "recent_requests": deque(maxlen=MAX_HISTORY)  # detailed logs
}

def record_request(success: bool, error_type: str = None):
    metrics_data["total_requests"] += 1

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "success": success,
        "error_type": error_type
    }
    metrics_data["recent_requests"].append(entry)

    if success:
        metrics_data["successful_requests"] += 1
    else:
        metrics_data["failed_requests"] += 1
        if error_type:
            metrics_data["errors_by_type"].setdefault(error_type, 0)
            metrics_data["errors_by_type"][error_type] += 1

def record_chaos_event(event_type: str):
    metrics_data["chaos_events"].append({
        "event": event_type,
        "timestamp": datetime.utcnow().isoformat()
    })
    # Optional: keep this list short
    if len(metrics_data["chaos_events"]) > MAX_HISTORY:
        metrics_data["chaos_events"].pop(0)

def get_metrics():
    return metrics_data
