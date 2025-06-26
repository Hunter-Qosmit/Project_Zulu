import requests

def get_backend_metrics(backend_url: str) -> dict:
    try:
        res = requests.get(f"{backend_url}/metrics", timeout=3)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"[Metrics] Failed to get metrics: {e}")
        return {}
