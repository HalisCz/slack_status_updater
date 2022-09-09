from datetime import datetime

from workalendar.europe import CzechRepublic


def is_workday(timestamp=datetime.now(), holidays_ignored=False):
    """
    Determines if timestamp moment is workday or not

    :param timestamp: datetime moment in question, defaults to now
    :param holidays_ignored: boolean to ignore holidays and recognize only weekend days
    :return: boolean True for working moment, False otherwise
    """

    # TODO get country from config
    workcal = CzechRepublic()
    # TODO get holidays condition from config

    # if holidays not ignored
    if holidays_ignored == False:
        if workcal.is_working_day(timestamp.date()):
            return True
        else:
            return False
    # if holidays ignored, consider only weekends
    else:
        if timestamp.date().weekday() <= 4:
            return True
        else:
            return False
