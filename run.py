import time
from datetime import datetime
import app
import os 

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def countdown(start_from):
    """"Counts down from specified minute value"""
    time_left = start_from
    while time_left > 0:
            print("Next check", time_left, "min")
            time.sleep(60)
            time_left -= 1

def run_script():

    while True:
        clear()
        print("\nChecking for new dates..")
        new_date_found = app.main()
        if new_date_found:
            break
        countdown(15) # 15min

if __name__ == "__main__":
    run_script()



