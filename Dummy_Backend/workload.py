import time
import random

def do_work(data):
    time.sleep(random.uniform(0.1, 0.5))  # Simulate some processing time
    return {"status": "processed", "echo": data}
