import time
import os 

def clear():
    """Clear terminal scren"""
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def wait(duration, attempt):
    """"Counts down from specified minute value"""
    time_left = duration
    while time_left > 0:
            clear()
            print("== No new dates yet. == (" + str(attempt) + ")")
            print("Next check in ", time_left, "min")
            time.sleep(60)
            time_left -= 1


