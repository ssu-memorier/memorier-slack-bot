from constants.COMMAND import *     # 상수

from utils.date import getCurrentSeoulTime
from utils.log import printCommandLogs, printWorkState


def GoToWork(message, say):  # !출근
    dates = getCurrentSeoulTime()       # 현재시간을 가져온다

    # 10시 10분 넘어서 출근을 하면 지각 처리
    if dates.time().hour >= 10 and dates.time().minute >= 10:
        state = LATE
    else:
        state = GTW

    workOutput = printWorkState(message, dates, state)

    printCommandLogs(message, ATTENDANCE_COMMAND[state])      # 로그 출력
    say(text=workOutput, channel=CHANNEL_ATTENDANCE)


def LeaveToWork(message, say):  # !퇴근
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, LTW)

    printCommandLogs(message, ATTENDANCE_COMMAND[LTW])      # 로그 출력
    say(text=workOutput, channel=CHANNEL_ATTENDANCE)


def OfflineWork(message, say):  # !오프 (시간)
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, OW)

    printCommandLogs(message, ATTENDANCE_COMMAND[OW])      # 로그 출력
    say(text=workOutput, channel=CHANNEL_ATTENDANCE)
