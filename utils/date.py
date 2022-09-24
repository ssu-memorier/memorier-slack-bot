# get Time
from datetime import datetime
from pytz import timezone
from constants import DATE


def getCurrentSeoulTime():
    return datetime.now(timezone(DATE.ASIA_SEOUL))
