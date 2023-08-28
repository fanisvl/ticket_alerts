import time
from datetime import datetime
import app

def run_script():
    while True:
        print("\nChecking for new dates..")
        new_date_found = app.main()
        if new_date_found:
            break
        print("Next check in 15min ")
        time.sleep(900) # run every 15min

if __name__ == "__main__":
    run_script()
