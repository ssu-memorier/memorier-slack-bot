# get Time
from datetime import datetime
from pytz import timezone
from constants import DATE


def getCityTime(city):      # 도시 시간 구하는 함수 (추후 사용 예정)
    return datetime.now(timezone(city)).strftime(DATE.DATE_FORMAT)


def getNowCityHourMinutes(city):      # 도시 시분 구하는 함수 (추후 사용 예정)
    times = datetime.now(timezone(city))
    return times.time().hour, times.time().minute


def ts2datetime(ts):        # Timestamp to Datetime
    return datetime.fromtimestamp(ts, timezone(DATE.ASIA_SEOUL)).strftime(DATE.DATE_FORMAT)


def getTs2HourMinute(ts):        # Timestamp to get Hour, Minute
    date = datetime.fromtimestamp(ts, timezone(DATE.ASIA_SEOUL)).time()
    return date.hour, date.minute
