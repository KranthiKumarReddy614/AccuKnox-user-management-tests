import os
import subprocess
import logging
from datetime import datetime

# ------------------ CONFIGURATION ------------------

# Directory to back up
SOURCE_DIR = "/path/to/local/directory"

# Remote details
REMOTE_USER = "username"
REMOTE_HOST = "your.remote.server"
REMOTE_DIR = "/path/to/remote/backup/"

# Optional: SSH key if required
SSH_KEY = "~/.ssh/id_rsa"

# Log file
LOG_FILE = "backup_report.log"

# ------------------ SETUP LOGGING ------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------ BACKUP FUNCTION ------------------

def run_backup():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_label = f"Backup @ {timestamp}"
    
    print(f"\n🔄 {backup_label}")
    logging.info(backup_label)

    rsync_command = [
        "rsync", "-avz", "--delete",
        "-e", f"ssh -i {SSH_KEY}",
        SOURCE_DIR,
        f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"
    ]

    try:
        result = subprocess.run(rsync_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        msg = f"✅ Backup succeeded.\nOutput:\n{result.stdout.decode()}"
        print(msg)
        logging.info(msg)
    except subprocess.CalledProcessError as e:
        error_msg = f"❌ Backup failed.\nError:\n{e.stderr.decode()}"
        print(error_msg)
        logging.error(error_msg)

# ------------------ MAIN ------------------

if __name__ == "__main__":
    run_backup()
