import time
from datetime import datetime
import check_availability
import os 

def clear():
    """Clear terminal scren"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def countdown(start_from, attempt):
    """"Counts down from specified minute value"""
    time_left = start_from
    while time_left > 0:
            clear()
            print("== No new dates yet. == (" + str(attempt) + ")")
            print("Next check in ", time_left, "min")
            time.sleep(60)
            time_left -= 1

def run_script():

    interval = int(input("Interval between checks (min)? "))
    attempt = 0
    while True:
        clear()
        attempt += 1
        print("\nChecking for new dates..")
        # pass interval here and implement the while loop inside check_availability
        new_date_found = check_availability.main() 
        if new_date_found:
            break
        countdown(interval, attempt)

if __name__ == "__main__":
    run_script()



