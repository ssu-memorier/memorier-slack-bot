from constants import DATE
from constants.COMMAND import *
from utils.date import getCurrentSeoulTime


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    user = message['user']
    currentTime = getCurrentSeoulTime().strftime(DATE.DATE_FORMAT)
    print(f"{currentTime}\t{user}가 {command} 명령어를 사용하였습니다")


def printWorkState(message, date, state):  # 출력할 메세지 생성기
    # 자리비움의 경우 시간까지 입력
    if state == OW:
        duringTime = message['text'].split()[1]     # 자리비움 시간
        return f"[ <@{message['user']}> ] {date.strftime(DATE.DATE_FORMAT)}\t{duringTime}시간 {ATTENDANCE_COMMAND[state][1:]}"
    else:
        return f"[ <@{message['user']}> ] {date.strftime(DATE.DATE_FORMAT)}\t{ATTENDANCE_COMMAND[state][1:]}"
