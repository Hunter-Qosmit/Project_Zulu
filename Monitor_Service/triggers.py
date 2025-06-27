from datetime import datetime, timedelta

last_ai_call_time = None
COOLDOWN_SECONDS = 900  # 15 minutes

def should_trigger_ai(metrics: dict) -> bool:
    global last_ai_call_time

    now = datetime.now(datetime.UTC)
    if last_ai_call_time and (now - last_ai_call_time) < timedelta(seconds=COOLDOWN_SECONDS):
        return False

    if metrics.get("failed_requests", 0) > 3:
        last_ai_call_time = now
        return True

    if "cpu_burn" in [e["event"] for e in metrics.get("chaos_events", [])]:
        last_ai_call_time = now
        return True

    return False
