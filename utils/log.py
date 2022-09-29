from constants import UTIL
from constants.COMMAND import ATTENDANCE, CHANNEL


def printCommandLogs(message, command):  # console에 Command 명령 log를 기록
    currentTime = message.date
    print(
        f"{currentTime}\t{UTIL.USER_NAME[message.userID]} 님이 {command} 명령어를 사용하였습니다")


def sayWorkState(say, message, state):  # 채널에 출력할 메세지 생성기
    # date : Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)

    if state == ATTENDANCE.OW:  # 자리비움의 경우 시간까지 입력
        # tokens = [커맨드(자리비움), 시간]
        [command, offTime] = message.text.split()

        text = f"[ <@{message.userID}> ] {message.date}\t{offTime}시간 {ATTENDANCE.COMMAND_NAME[state]}"
    else:
        text = f"[ <@{message.userID}> ] {message.date}\t{ATTENDANCE.COMMAND_NAME[state]}"

    sayToAttendanceChannel(say, text)


def sayToAttendanceChannel(say, text):     # 채널에 메세지 출력
    say(text=text, channel=CHANNEL.ATTENDANCE)


def sayToHelpChannel(say, text):     # 개인 채널에 도움말 메세지 출력
    say(text=text, channel=CHANNEL.BOT)
