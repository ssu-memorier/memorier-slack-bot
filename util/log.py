from constants import DATE
from util.date import getCurrentSeoulTime


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    user = message['user']
    currentTime = getCurrentSeoulTime().strftime(DATE.DATE_FORMAT)
    print(f"{currentTime}\t{user}가 {command} 명령어를 사용하였습니다")
