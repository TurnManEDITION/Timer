import os, time


def edit_data(local_data):
    if local_data[0] == "Mon": local_data[0] = "Monday"
    if local_data[0] == "Tue": local_data[0] = "Tuesday"
    if local_data[0] == "Wed": local_data[0] = "Wednesday"
    if local_data[0] == "Thu": local_data[0] = "Thursday"
    if local_data[0] == "Fri": local_data[0] = "Friday"
    if local_data[0] == "Sat": local_data[0] = "Saturday"
    if local_data[0] == "Sun": local_data[0] = "Sunday"

    if local_data[1] == "Dec": local_data[1] = "December"
    if local_data[1] == "Jan": local_data[1] = "January"
    if local_data[1] == "Feb": local_data[1] = "February"
    if local_data[1] == "Mar": local_data[1] = "March"
    if local_data[1] == "Apr": local_data[1] = "April"
    if local_data[1] == "May": local_data[1] = "May"
    if local_data[1] == "Jun": local_data[1] = "June"
    if local_data[1] == "Jul": local_data[1] = "July"
    if local_data[1] == "Aug": local_data[1] = "August"
    if local_data[1] == "Sep": local_data[1] = "September"
    if local_data[1] == "Oct": local_data[1] = "October"
    if local_data[1] == "Nov": local_data[1] = "November"
    return local_data


def breaks():
    pass


def check_timer(timer):
    timer = str(timer).split(":")
    hours = int(timer[0])
    minutes = int(timer[1])
    seconds = int(timer[2])

    timer = [hours, minutes, seconds]
    
    if timer[2] == -1:
        timer[2] = 59
        timer[1] -= 1
    if timer[1] == -1:
        timer[1] = 59
        timer[0] -= 1
    if timer[0] == 0 and timer[1] == 0 and timer[2] == 0:
        breaks()
    timer = f"{timer[0]}:{timer[1]}:{timer[2]}"
    return timer



def edit_timer(timer):
    timer = check_timer(timer)
    timer = str(timer).split(":")
    hours = int(timer[0])
    minutes = int(timer[1])
    seconds = int(timer[2])
    if seconds > 59:
        minutes += seconds // 60
        seconds -= 60 * (seconds // 60) 
    if minutes > 59:
        hours += minutes // 60
        minutes -= 60 * (minutes // 60)
    timer = [hours, minutes, seconds]
    if len(str(timer[2])) < 2:
        timer[2] = "0" + str(timer[2])
    if len(str(timer[1])) < 2:
        timer[1] = "0" + str(timer[1])
    if len(str(timer[0])) < 2:
        timer[0] = "0" + str(timer[0])
    timer = f"{timer[0]}:{timer[1]}:{timer[2]}"
    return timer
    

def work_timer(timer):
    timer = str(timer).split(":")
    hours = int(timer[0])
    minutes = int(timer[1])
    seconds = int(timer[2])

    timer = [hours, minutes, seconds]
    timer[2] -= 1
    
    timer = f"{timer[0]}:{timer[1]}:{timer[2]}"
    timer = edit_timer(timer)
    return timer