import threading
import psutil

def capture():
    while getattr(threading.current_thread(), 'running', True):
        with open(f'capture_result.txt', 'a') as f:
            f.write(f'{getattr(threading.current_thread(), "status", "unknown")},{psutil.cpu_percent()},{psutil.virtual_memory().used}\n')
