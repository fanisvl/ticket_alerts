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
            clear()
            print("== No new dates yet. == ")
            print("Next check in ", time_left, "min")
            time.sleep(60)
            time_left -= 1

def run_script():

    interval = int(input("Interval between checks (min)? "))
    attempts = 0
    while True:
        clear()
        attempts += 1
        print("\nChecking for new dates.. (" + str(attempts) + ")")
        new_date_found = app.main()
        if new_date_found:
            break
        countdown(interval)

if __name__ == "__main__":
    run_script()



