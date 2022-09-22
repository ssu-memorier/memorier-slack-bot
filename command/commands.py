import re       # 정규식

from constants.COMMAND import *
from command import help


def addAttendanceCommand(app):

    @app.message(re.compile(ATTENDANCE_COMMAND[HELP]))    # !도움말
    def say_comment_help(message, say):
        help.helpCommand(message, say)
