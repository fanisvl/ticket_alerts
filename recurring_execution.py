import time
from datetime import datetime
import app

def run_script():
    print()
    print("Checking for new dates..")
    app.main()


def main():
    while True:
        run_script()
        print("\nNext check in 15min ")
        time.sleep(900) # run every 15min

if __name__ == "__main__":
    main()
