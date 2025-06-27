from fastapi import FastAPI, Request
from dotenv import load_dotenv
import logging
from ai_engine import analyze_metrics

load_dotenv()

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

app = FastAPI()

@app.post("/analyze")
async def analyze(request: Request):
    body = await request.json()
    log.info(f"Received metrics from monitor: {body}")

    summary = analyze_metrics(body.get("metrics", {}))
    return {"status": "ok", "summary": summary}
