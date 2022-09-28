from constants import COMMAND, TOKEN     # 날짜, 커맨드 상수
from utils.date import getCurrentSeoulTime


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    currentTime = getCurrentSeoulTime()
    print(
        f"{currentTime}\t{TOKEN.USER_NAME[message.userID]} 님이 {command} 명령어를 사용하였습니다")


def printWorkState(message, date, state):  # 채널에 출력할 메세지 생성기
    # date : Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)

    if state == COMMAND.OW:  # 자리비움의 경우 시간까지 입력
        # tokens = [커맨드(자리비움), 시간]
        [command, offTime] = message.text.split()

        return f"[ <@{message.userID}> ] {date}\t{offTime}시간 {COMMAND.ATTENDANCE_COMMAND_NAME[state]}"
    else:
        return f"[ <@{message.userID}> ] {date}\t{COMMAND.ATTENDANCE_COMMAND_NAME[state]}"
