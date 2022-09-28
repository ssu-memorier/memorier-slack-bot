# get Time
from datetime import datetime
from pytz import timezone
from constants import DATE


def getCurrentSeoulTime():
    return datetime.now(timezone(DATE.ASIA_SEOUL)).strftime(DATE.DATE_FORMAT)


def getCurrentSeoulHourMinutes():
    times = datetime.now(timezone(DATE.ASIA_SEOUL))
    return times.time().hour, times.time().minute
