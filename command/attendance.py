from constants import DATE
from constants.COMMAND import ATTENDANCE     # 상수

from utils.log import printCommandLogs, sayWorkState, sayToAttendanceChannel


def goToWork(message, say):  # !출근
    hour, minutes = message.hour, message.minute   # 명령어를 실행한 시(HH), 분(MM)

    # 10시 10분 넘어서 출근을 하면 지각 처리
    if hour >= DATE.LATE_TIME[DATE.HOUR] and minutes >= DATE.LATE_TIME[DATE.MIN]:
        state = ATTENDANCE.LATE
    else:
        state = ATTENDANCE.GTW

    sayWorkState(say, message, state)   # 채널 출력
    printCommandLogs(
        message, ATTENDANCE.COMMAND_NAME[state])      # 로그 출력


def leaveToWork(message, say):  # !퇴근
    sayWorkState(say, message, ATTENDANCE.LTW)   # 채널 출력
    printCommandLogs(
        message, ATTENDANCE.COMMAND_NAME[ATTENDANCE.LTW])      # 로그 출력


def offlineWork(message, say):  # !오프 (시간)
    sayWorkState(say, message, ATTENDANCE.OW)   # 채널 출력
    printCommandLogs(
        message, ATTENDANCE.COMMAND_NAME[ATTENDANCE.OW])      # 로그 출력
