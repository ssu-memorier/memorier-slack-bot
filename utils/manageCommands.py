import re       # 정규식

from constants.COMMAND import *
from command.help import *      # help 명령어
from command.attendance import *        # 출석 관련 명령어


def addHelpCommand(app):      # 도움말 관련 명령어 추가

    @app.message(re.compile(ATTENDANCE_COMMAND[HELP]))    # !도움말
    def say_comment_help(message, say):
        helpCommand(message, say)


def addAttendanceCommand(app):      # 출석 관련 명령어 추가

    @app.message(re.compile(ATTENDANCE_COMMAND[GTW]))  # !출근
    def say_comment_gotowork(message, say):
        GoToWork(message, say)

    @app.message(re.compile(ATTENDANCE_COMMAND[LTW]))  # !퇴근
    def say_comment_leavetowork(message, say):
        LeaveToWork(message, say)

    @app.message(re.compile(OFFLINE))  # !오프 (시간)
    def say_comment_off(message, say):
        OfflineWork(message, say)


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addHelpCommand(app)
    addAttendanceCommand(app)
