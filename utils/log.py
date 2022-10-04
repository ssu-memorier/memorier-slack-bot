from constants import USER


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    currentTime = message.date
    print(
        f"{currentTime}\t{USER.NAME[message.userID]} 님이 {command} 명령어를 사용하였습니다")
