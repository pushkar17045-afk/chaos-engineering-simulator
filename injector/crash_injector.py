# injector/crash_injector.py
import os
import signal

def crash_container(pid):
    os.kill(pid, signal.SIGKILL)
