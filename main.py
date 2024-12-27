import os, time
from edit import *


os.system("cls")
while True:
    try:
        hours = int(input(f"Hours: "))
        if not hours < 0:
            os.system("cls")
            break
        else:
            os.system("cls")
    except ValueError:
        os.system("cls")
while True:
    try:
        minutes = int(input(f"Hours: {hours}; minutes: "))
        if not minutes < 0:
            os.system("cls")
            break
        else:
            os.system("cls")
    except ValueError:
        os.system("cls")
while True:
    try:
        seconds = int(input(f"Hours: {hours}; minutes: {minutes}; seconds: "))
        if not seconds < 0:
            os.system("cls")
            break
        else:
            os.system("cls")
    except ValueError:
        os.system("cls")
timer = f"{hours}:{minutes}:{seconds}"
timer = edit_timer(timer)
while not timer == "00:00:00":
    local_data = edit_data(time.asctime().split())
    local_data = " | ".join(local_data)
    print(local_data)
    print(f"Timer - {timer}")
    timer = edit_timer(timer)
    timer = work_timer(timer)  
    time.sleep(1)
    os.system("cls")