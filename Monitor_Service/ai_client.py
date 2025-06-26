import requests
import os

AI_ENDPOINT = os.getenv("AI_MICROSERVICE_URL", "http://localhost:9000/analyze")

def send_to_ai(metrics: dict):
    try:
        print("[AI Client] Sending data to AI service...")
        res = requests.post(AI_ENDPOINT, json={"metrics": metrics}, timeout=5)
        res.raise_for_status()
        print(f"[AI Client] AI Response: {res.json()}")
    except Exception as e:
        print(f"[AI Client] Failed to send to AI service: {e}")
