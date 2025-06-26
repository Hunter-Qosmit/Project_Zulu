import os
import random
import sys
import time
from threading import Thread

# Load chaos parameters
FAULT_PROB = float(os.getenv("FAULT_PROBABILITY", 0.3))
MAX_DELAY = int(os.getenv("MAX_DELAY_SECONDS", 2))

# Keep references so the memory doesn't get garbage collected
_active_memory_threads = []

def _allocate_memory(size_mb: int, duration: int):
    print(f"[CHAOS] Holding ~{size_mb}MB of memory for {duration}s")
    # Allocate memory
    junk = [bytearray(1024 * 1024) for _ in range(size_mb)]

    time.sleep(duration)

    # Optional: Clear memory (not really necessary in short-lived process)
    del junk
    print(f"[CHAOS] Released {size_mb}MB of memory")

def simulate_memory_hold(size_mb: int = 200, duration_seconds: int = 60):
    t = Thread(target=_allocate_memory, args=(size_mb, duration_seconds), daemon=True)
    t.start()
    _active_memory_threads.append(t)

def maybe_fail():
    chance = random.random()

    if chance < FAULT_PROB:
        fail_type = random.choice(["cpu", "mem", "timeout", "http_error", "crash"])
        print(f"[CHAOS] Injecting failure: {fail_type}")

        if fail_type == "cpu":
            [x ** 2 for x in range(10**6)]
        elif fail_type == "mem":
            _ = [bytearray(1024 * 1024) for _ in range(100)]
        elif fail_type == "timeout":
            time.sleep(MAX_DELAY)
        elif fail_type == "http_error":
            raise Exception("Simulated 500 error")
        elif fail_type == "crash":
            sys.exit(1)

def simulate_cpu_spike():
    [x ** 2 for x in range(10**6)]

def _hover_cpu(target_percent=50, duration=60):
    work_time = 0.05  # base time unit
    sleep_time = work_time * ((100 - target_percent) / target_percent)
    end_time = time.time() + duration

    while time.time() < end_time:
        start = time.time()
        while time.time() - start < work_time:
            _ = [x**2 for x in range(1000)]
        time.sleep(sleep_time)

def simulate_cpu_hover(percent=50, duration_seconds=60, cores=1):
    print(f"[CHAOS] Hovering CPU at ~{percent}% on {cores} core(s) for {duration_seconds} seconds")
    for _ in range(cores):
        Thread(target=_hover_cpu, args=(percent, duration_seconds), daemon=True).start()

def simulate_mem_spike():
    _ = [bytearray(1024 * 1024) for _ in range(100)]

def simulate_timeout(seconds=2):
    time.sleep(seconds)

def simulate_crash():
    sys.exit(1)

def simulate_http_error():
    raise Exception("Simulated internal server error")

def simulate_cpu_loop():
    while True:
        [x ** 2 for x in range(10**6)]

def simulate_mem_loop():
    data = []
    while True:
        data.append(bytearray(1024 * 1024))  # 1MB chunks
        time.sleep(0.1)
