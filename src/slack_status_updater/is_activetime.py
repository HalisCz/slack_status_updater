from datetime import datetime


def is_activetime(schedule, timestamp=datetime.now()):
    """
    Determines if timestamp moment is in active timeslot or not

    :param schedule: object with current schedule
    :param timestamp: datetime of a moment in question, defaults to now
    :return: boolean True for active time moment, False otherwise
    """

    schedule = schedule["schedule"]

    weekday_name = timestamp.date().strftime("%A").lower()

    # find out if there is a workingtime schedule for this weekday
    schedule_selected = ""
    if weekday_name in schedule:
        schedule_selected = schedule[weekday_name]
    # find out if there is a workingtime schedule for default day
    elif "default" in schedule:
        schedule_selected = schedule["default"]
    else:
        return False

    # parse time intervals
    time_intervals = []
    for interval in schedule_selected:
        start, stop = str(interval).split("-", 1)
        start = datetime.strptime(start, "%H:%M").time()
        stop = datetime.strptime(stop, "%H:%M").time()
        time_intervals.append([start, stop])

    # check if timestamp fits in some interval
    timestamp = timestamp.time()
    for interval in time_intervals:
        if timestamp >= interval[0] and timestamp < interval[1]:
            return True
    else:
        return False
