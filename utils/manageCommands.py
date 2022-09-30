import re       # 정규식

from constants.COMMAND import IDENTIFIER, BASE
from utils import date, sayCommand, log, printError


class AppMessage():     # app으로 부터 받은 메시지 정보를 관리하는 클래스
    def __init__(self, message):
        self.channel = message['channel']
        self.text = message['text']
        self.userID = message['user']

        # 명령어가 실행된 날짜값 저장
        self.ts = message['ts']     # timestamp
        self.date = date.ts2datetime(float(message['ts']))      # datetime
        self.hour, self.minute = date.getTs2HourMinute(
            float(message['ts']))    # HH, MM


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addEMCommands(app)       # '!'로 시작하는 명령어 추가


def addEMCommands(app):      # Commands startswith '!'
    @app.message(re.compile("^[!]"))
    def CommandWork(message, say):
        message = AppMessage(message)   # 객체 변환

        if isHelpCommand(message):   # Help 명령어 확인
            controlHelpCommand(message, say)
        elif isAttendanceCommand(message):   # Attendance 명령어 확인
            controlAttendanceCommand(message, say)
        else:
            printError.commandInputError(say)


def controlHelpCommand(message, say):      # 도움 관련 명령어 제어문
    text, command = sayCommand.Help(message, say)

    if command != BASE.ERROR:
        log.sayHelpChannel(say, text)     # 채널에 출력
        log.printCommandLogs(message, command)    # 콘솔에 로그 출력


def controlAttendanceCommand(message, say):      # 출석 관련 명령어 제어문
    if message.text.startswith(IDENTIFIER.GOTOWORK):    # !출근
        text, command = sayCommand.Gotowork(message, say)
    elif message.text.startswith(IDENTIFIER.LEAVETOWORK):  # !퇴근
        text, command = sayCommand.Leavetowork(message, say)
    elif message.text.startswith(IDENTIFIER.OFFLINE):   # !오프
        text, command = sayCommand.Offline(message, say)
    else:
        printError.commandInputError(say)   # 명령어 입력 에러
        command = BASE.ERROR

    if command != BASE.ERROR:
        log.sayAttendanceChannel(say, text)     # 채널에 출력
        log.printCommandLogs(message, command)    # 콘솔에 로그 출력


def isAttendanceCommand(message):   # Attendance 명령어인지 확인하는 함수
    # Attendance 명령어 리스트를 하나씩 확인하며 해당 명령어가 있는지 확인
    for identifier in IDENTIFIER.ATTENDANCE:
        if message.text.startswith(identifier):
            return True
    else:
        return False


def isHelpCommand(message):  # help 명령어인지 확인하는 함수
    # help 명령어 인지 확인
    return True if message.text.startswith(IDENTIFIER.HELP) else False
