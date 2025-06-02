import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds
CPU_THRESHOLD = 80.0       # percent
MEM_THRESHOLD = 80.0       # percent
DISK_THRESHOLD = 90.0      # percent
PROC_THRESHOLD = 300       # number of processes

def log_alert(message):
    print("ALERT:", message)
    logging.warning(message)

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {usage}%")
    return usage

def check_memory():
    mem = psutil.virtual_memory()
    usage = mem.percent
    if usage > MEM_THRESHOLD:
        log_alert(f"High memory usage detected: {usage}%")
    return usage

def check_disk():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        log_alert(f"Low disk space on '/': {usage}% used")
    return usage

def check_processes():
    count = len(psutil.pids())
    if count > PROC_THRESHOLD:
        log_alert(f"Too many running processes: {count}")
    return count

def monitor_system():
    print(f"\n[{datetime.now()}] System Health Check Running...\n")
    
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    procs = check_processes()
    
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {procs}")

if __name__ == "__main__":
    monitor_system()
