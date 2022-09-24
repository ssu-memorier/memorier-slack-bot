from constants.COMMAND import *     # 상수
from constants.DATE import *

from utils.date import getCurrentSeoulTime
from utils.log import printCommandLogs, printWorkState, printCommandLogsInCoreTime


def GoToWork(message, say):  # !출근
    dates = getCurrentSeoulTime()       # 현재시간을 가져온다
    hour, minutes = dates.time().hour, dates.time().minute   # 명령어를 실행한 시(HH), 분(MM)

    # 10시 10분 넘어서 출근을 하면 지각 처리
    if hour >= LATE_TIME[HOUR] and minutes >= LATE_TIME[MIN]:
        state = LATE
    else:
        state = GTW

    workOutput = printWorkState(message, dates, state)

    printCommandLogs(message, ATTENDANCE_COMMAND[state])      # 로그 출력
    say(text=workOutput, channel=CHANNEL_ATTENDANCE)


def LeaveToWork(message, say):  # !퇴근
    state = LTW
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    hour = date.time().hour         # 명령어를 실행한 시(HH)

    # 코어타임 이전에 퇴근을 시도하는 경우
    if CORETIME[START_TIME][HH] <= hour < CORETIME[END_TIME][HH]:
        printCommandLogsInCoreTime(message, state)      # 로그에 해당내용 기록
        workOutput = CORETIME_OUTPUT[state]        # 해당 명령어 입력하는 부분에 경고문 출력

        # message['channel'] : 현재 봇과 대화하는 채널
        say(text=workOutput, channel=message['channel'])

    else:
        workOutput = printWorkState(message, date, LTW)

        printCommandLogs(message, ATTENDANCE_COMMAND[LTW])      # 로그 출력
        say(text=workOutput, channel=CHANNEL_ATTENDANCE)


def OfflineWork(message, say):  # !오프 (시간)
    state = OW
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    hour = date.time().hour         # 명령어를 실행한 시(HH)

    if CORETIME[START_TIME][HH] <= hour < CORETIME[END_TIME][HH]:
        printCommandLogsInCoreTime(message, state)      # 로그에 해당내용 기록
        workOutput = CORETIME_OUTPUT[state]        # 해당 명령어 입력하는 부분에 경고문 출력

        # message['channel'] : 현재 봇과 대화하는 채널
        say(text=workOutput, channel=message['channel'])

    else:
        workOutput = printWorkState(message, date, OW)

        printCommandLogs(message, ATTENDANCE_COMMAND[OW])      # 로그 출력
        say(text=workOutput, channel=CHANNEL_ATTENDANCE)
