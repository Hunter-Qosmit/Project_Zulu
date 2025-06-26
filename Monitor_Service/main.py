import time
import os
from dotenv import load_dotenv
from metrics import get_backend_metrics
from triggers import should_trigger_ai
from ai_client import send_to_ai

load_dotenv()

BACKEND_URL = os.getenv("DUMMY_BACKEND_URL", "http://localhost:8000")

def run_monitor():
    print("[Monitor] Starting monitor loop...")
    while True:
        metrics = get_backend_metrics(BACKEND_URL)
        if should_trigger_ai(metrics):
            send_to_ai(metrics)
        time.sleep(10)

if __name__ == "__main__":
    run_monitor()
