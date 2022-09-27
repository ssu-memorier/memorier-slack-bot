from constants import DATE, COMMAND     # 날짜, 커맨드 상수
from utils.date import getCurrentSeoulTime


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    user = message['user']
    currentTime = getCurrentSeoulTime().strftime(DATE.DATE_FORMAT)
    print(f"{currentTime}\t{user}가 {command} 명령어를 사용하였습니다")


def printWorkState(message, date, state):  # 출력할 메세지 생성기
    # Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)
    commandWorkDate = date.strftime(DATE.DATE_FORMAT)
    userID = message['user']        # 유저 ID

    if state == COMMAND.OW:  # 자리비움의 경우 시간까지 입력
        # tokens = [커맨드(자리비움), 시간]
        [command, offTime] = message['text'].split()

        return f"[ <@{userID}> ] {commandWorkDate}\t{offTime}시간 {COMMAND.ATTENDANCE_COMMAND_NAME[state]}"
    else:
        return f"[ <@{userID}> ] {commandWorkDate}\t{COMMAND.ATTENDANCE_COMMAND_NAME[state]}"
