# get Time
from datetime import datetime
import time
from pytz import timezone

from constants import DATE


''' Get datetime using timezone '''


def getCityTime(city):      # 도시 시간 구하는 함수 (추후 사용 예정)
    return datetime.now(timezone(city)).strftime(DATE.DATE_FORMAT)


def getNowCityHourMinutes(city):      # 도시 시분 구하는 함수 (추후 사용 예정)
    times = datetime.now(timezone(city))
    return times.time().hour, times.time().minute


''' timestamp <- convert -> datetime '''


def ts2datetime(ts):        # Timestamp to Datetime
    return datetime.fromtimestamp(ts, timezone(DATE.ASIA_SEOUL)).strftime(DATE.DATE_FORMAT)


def getTs2HourMinute(ts):        # Timestamp to get Hour, Minute
    date = datetime.fromtimestamp(ts, timezone(DATE.ASIA_SEOUL)).time()
    return date.hour, date.minute


''' Calculate the time between '''


def isTimeInBetween(timestamp, baseTime):   # 해당 시간이 구하고자하는 시간 사이에 있는가
    checkdate = datetime.fromtimestamp(
        float(timestamp), timezone(DATE.ASIA_SEOUL)).date()  # 오늘 날짜값 추출

    startTime = datetime(checkdate.year, checkdate.month, checkdate.day,
                         baseTime[DATE.START_TIME][DATE.HOUR],
                         baseTime[DATE.START_TIME][DATE.MIN], 0)
    startTimestamp = time.mktime(
        startTime.timetuple()) - DATE.DIFF_TIMESTAMP_GMT9  # 기준 시작시간

    endTime = datetime(checkdate.year, checkdate.month, checkdate.day,
                       baseTime[DATE.END_TIME][DATE.HOUR],
                       baseTime[DATE.END_TIME][DATE.MIN], 0)
    endTimestamp = time.mktime(endTime.timetuple()) - \
        DATE.DIFF_TIMESTAMP_GMT9  # 기준 종료시간

    return True if startTimestamp <= float(timestamp) <= endTimestamp else False
