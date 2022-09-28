from constants import DATE
from constants.COMMAND import ATTENDANCE     # 상수

from utils.log import printCommandLogs, printWorkState, sayToAttendanceChannel


def GoToWork(message, say):  # !출근
    hour, minutes = message.HOUR, message.MINUTE   # 명령어를 실행한 시(HH), 분(MM)

    # 10시 10분 넘어서 출근을 하면 지각 처리
    if hour >= DATE.LATE_TIME[DATE.HOUR] and minutes >= DATE.LATE_TIME[DATE.MIN]:
        state = ATTENDANCE.LATE
    else:
        state = ATTENDANCE.GTW

    workOutput = printWorkState(message, state)

    printCommandLogs(
        message, ATTENDANCE.ATTENDANCE_COMMAND_NAME[state])      # 로그 출력
    sayToAttendanceChannel(say, workOutput)


def LeaveToWork(message, say):  # !퇴근
    workOutput = printWorkState(message, ATTENDANCE.LTW)

    printCommandLogs(
        message, ATTENDANCE.ATTENDANCE_COMMAND_NAME[ATTENDANCE.LTW])      # 로그 출력
    sayToAttendanceChannel(say, workOutput)


def OfflineWork(message, say):  # !오프 (시간)
    workOutput = printWorkState(message, ATTENDANCE.OW)

    printCommandLogs(
        message, ATTENDANCE.ATTENDANCE_COMMAND_NAME[ATTENDANCE.OW])      # 로그 출력
    sayToAttendanceChannel(say, workOutput)
