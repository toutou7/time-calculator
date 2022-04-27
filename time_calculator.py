days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def hour(time):
    try:
        if(time.split(":")[1].split(" ")[1] == "AM"):
            return int(time.split(":")[0])
        elif(time.split(":")[1].split(" ")[1] == "PM"):
            return int(time.split(":")[0]) + 12
    except IndexError:
        return int(time.split(":")[0])
    
def minute(time):
    return int(time.split(":")[1].split(" ")[0])

def hour_remainder(hour):
    if(hour%12 == 0):
        return "12"
    else:
        return str(hour%12)

def minute_remainder(minute):
    if(minute%60 == 0 or minute%60<10):
        return "0" + str(minute%60)
    else:
        return str(minute%60)

def is_in_the_morning(hour):
    if(hour/12 < 1):
        return "AM"
    else:
        return "PM"

def is_in_next_day(hour):
    if(hour/24 >= 1):
        return True
    else:
        return False

def day_difference(hour):
    message = ""
    if(is_in_next_day(hour)):
        if(int(hour/24) == 1):
            message += " (next day)"
        else:
            message += " (" + str(int(hour/24)) + " days later)"
    return message
    
def add_time(time1, time2, day=""):
    total_minute = minute(time1) + minute(time2)
    total_hour = int(hour(time1) + hour(time2) + total_minute/60)
    message = hour_remainder(total_hour) + ":" + minute_remainder(total_minute)
    message += " " + is_in_the_morning(total_hour%24)
    day = day.casefold().capitalize()
    if day in days_of_the_week:
        message += ", " + days_of_the_week[(days_of_the_week.index(day) + int(total_hour/24))%7]
    message += day_difference(total_hour)
    return message