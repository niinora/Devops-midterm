import requests
import time
from datetime import datetime
import sys

def check_health(url="http://localhost:5000"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, "Application is healthy"
        return False, f"Unhealthy response code: {response.status_code}"
    except requests.RequestException as e:
        return False, f"Error connecting to application: {str(e)}"

def log_status(status, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {'HEALTHY' if status else 'UNHEALTHY'}: {message}\n"
    
    print(log_entry.strip())
    with open("health_log.txt", "a") as f:
        f.write(log_entry)

def main():
    print("Starting health check monitoring...")
    while True:
        status, message = check_health()
        log_status(status, message)
        
        if not status:
            sys.exit(1)
            
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main() 