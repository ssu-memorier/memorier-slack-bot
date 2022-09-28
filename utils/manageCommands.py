import re       # 정규식

from constants import COMMAND       # 상수
from command import help, attendance      # help, 출석 관련 명령어


class appMessage():     # app으로 부터 받은 메시지 정보를 관리하는 클래스
    def __init__(self, message):
        self.channel = message['channel']
        self.text = message['text']
        self.ts = message['ts']
        self.userID = message['user']


def addHelpCommand(app):      # 도움말 관련 명령어 추가

    # !도움말
    @app.message(re.compile(COMMAND.HELP_REG))
    def sayCommentHelp(message, say):
        help.helpCommand(appMessage(message), say)


def addAttendanceCommand(app):      # 출석 관련 명령어 추가

    @app.message(re.compile(COMMAND.GOTOWORK_REG))  # !출근
    def sayCommentGotowork(message, say):
        attendance.GoToWork(appMessage(message), say)

    @app.message(re.compile(COMMAND.LEAVETOWORK_REG))  # !퇴근
    def sayCommentLeavetowork(message, say):
        attendance.LeaveToWork(appMessage(message), say)

    @app.message(re.compile(COMMAND.OFFLINE_REG))  # !오프 (시간)
    def sayCommentOff(message, say):
        attendance.OfflineWork(appMessage(message), say)


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addHelpCommand(app)
    addAttendanceCommand(app)
