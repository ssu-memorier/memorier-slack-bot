import re       # 정규식

from constants import COMMAND
from command import help, attendance      # help, 출석 관련 명령어


def addHelpCommand(app):      # 도움말 관련 명령어 추가

    # !도움말
    @app.message(re.compile(COMMAND.ATTENDANCE_COMMAND[COMMAND.HELP]))
    def sayCommentHelp(message, say):
        help.helpCommand(message, say)


def addAttendanceCommand(app):      # 출석 관련 명령어 추가

    @app.message(re.compile(COMMAND.ATTENDANCE_COMMAND[COMMAND.GTW]))  # !출근
    def sayCommentGotowork(message, say):
        attendance.GoToWork(message, say)

    @app.message(re.compile(COMMAND.ATTENDANCE_COMMAND[COMMAND.LTW]))  # !퇴근
    def sayCommentLeavetowork(message, say):
        attendance.LeaveToWork(message, say)

    @app.message(re.compile(COMMAND.OFFLINE_REG))  # !오프 (시간)
    def sayCommentOff(message, say):
        attendance.OfflineWork(message, say)


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addHelpCommand(app)
    addAttendanceCommand(app)
