import re       # 정규식

from constants import ERROR
from utils import error

from classes.AppMessge import AppMessage
from classes.Help import Help
from commands import help, attendance


def addAllCommands(app):      # 모든 Command가 실행되도록 추가
    @app.message(re.compile("^[!]"))
    def CommandWork(message, say):
        msg = AppMessage(message)   # 객체 변환

        if help.isHelpCommand(msg):   # Help 명령어 확인
            command = Help(msg, say)
        elif attendance.isAttendanceCommand(msg):   # Attendance 명령어 확인
            command = attendance.createAttendanceCommand(msg, say)
        else:
            error.sayError(say, ERROR.INPUT_ERROR)
            return

        command.sayCommand()
