from constants import COMMAND, DATE     # 상수

from utils.date import getCurrentSeoulTime, getCurrentSeoulHourMinutes
from utils.log import printCommandLogs, printWorkState


def GoToWork(message, say):  # !출근
    dates = getCurrentSeoulTime()       # 현재시간을 가져온다
    hour, minutes = getCurrentSeoulHourMinutes()   # 명령어를 실행한 시(HH), 분(MM)

    # 10시 10분 넘어서 출근을 하면 지각 처리
    if hour >= DATE.LATE_TIME[DATE.HOUR] and minutes >= DATE.LATE_TIME[DATE.MIN]:
        state = COMMAND.LATE
    else:
        state = COMMAND.GTW

    workOutput = printWorkState(message, dates, state)

    printCommandLogs(
        message, COMMAND.ATTENDANCE_COMMAND_NAME[state])      # 로그 출력
    say(text=workOutput, channel=COMMAND.CHANNEL_ATTENDANCE)


def LeaveToWork(message, say):  # !퇴근
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, COMMAND.LTW)

    printCommandLogs(
        message, COMMAND.ATTENDANCE_COMMAND_NAME[COMMAND.LTW])      # 로그 출력
    say(text=workOutput, channel=COMMAND.CHANNEL_ATTENDANCE)


def OfflineWork(message, say):  # !오프 (시간)
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, COMMAND.OW)

    printCommandLogs(
        message, COMMAND.ATTENDANCE_COMMAND_NAME[COMMAND.OW])      # 로그 출력
    say(text=workOutput, channel=COMMAND.CHANNEL_ATTENDANCE)
