# injector/latency_injector.py
import time

def inject_latency(seconds=3):
    print(f"[INJECTOR] Injecting {seconds}s latency")
    time.sleep(seconds)
