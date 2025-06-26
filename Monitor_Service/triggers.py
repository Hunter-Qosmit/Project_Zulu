def should_trigger_ai(metrics: dict) -> bool:
    if not metrics:
        return False

    fail_threshold = 3
    cpu_warning = 80.0  # Not yet implemented but plan for it

    if metrics.get("failed_requests", 0) > fail_threshold:
        print("[Triggers] Failed request threshold exceeded")
        return True

    return False
