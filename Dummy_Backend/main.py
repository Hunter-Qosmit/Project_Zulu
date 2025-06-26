from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from threading import Thread
from dotenv import load_dotenv
import os
from Dummy_Backend.workload import do_work
from Dummy_Backend import chaos
from Dummy_Backend.metrics import record_request, get_metrics, record_chaos_event

# Load environment variables from .env
load_dotenv(dotenv_path="Dummy_Backend/.env")

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Dummy backend running."}

@app.post("/process")
async def process_data(request: Request):
    try:
        chaos.maybe_fail()
        payload = await request.json()
        result = do_work(payload)
        record_request(success=True)
        return {"success": True, "result": result}
    except HTTPException as e:
        record_request(success=False)
        raise e
    except Exception as e:
        record_request(success=False)
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/metrics")
def metrics():
    return get_metrics()
@app.get("/health")
def health_check():
    try:
        return {"status": "healthy"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/force/hover_cpu")
def hover_cpu(percent: int = 50, duration: int = 60, cores: int = 1):
    record_chaos_event("hover_cpu")
    chaos.simulate_cpu_hover(percent=percent, duration_seconds=duration, cores=cores)
    return {
        "status": "CPU hovering started",
        "percent": percent,
        "duration_seconds": duration,
        "cores": cores
    }

@app.get("/force/hover_mem")
def hover_memory(size_mb: int = 200, duration: int = 60):
    record_chaos_event("hover_mem")
    chaos.simulate_memory_hold(size_mb=size_mb, duration_seconds=duration)
    return {
        "status": "Memory pressure started",
        "size_mb": size_mb,
        "duration_seconds": duration
    }

    
@app.get("/force/{failure_type}")
def force_failure(failure_type: str):
    if failure_type == "cpu":
        record_chaos_event("cpu_spike")
        chaos.simulate_cpu_spike()
    elif failure_type == "mem":
        record_chaos_event("mem_spike")
        chaos.simulate_mem_spike()
    elif failure_type == "crash":
        record_chaos_event("crash")
        chaos.simulate_crash()
    elif failure_type == "error":
        record_chaos_event("error")
        chaos.simulate_http_error()
    elif failure_type == "loop_cpu":
        record_chaos_event("loop_cpu")
        Thread(target=chaos.simulate_cpu_loop).start()
    elif failure_type == "loop_mem":
        record_chaos_event("loop_mem")
        Thread(target=chaos.simulate_mem_loop).start()
    else:
        raise HTTPException(status_code=400, detail="Invalid failure type")

    return {"status": f"{failure_type} triggered"}