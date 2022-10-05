import re       # 정규식

from constants import ERROR
from utils import error

from classes import AppMessage
from commands import help, attendance


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addEMCommands(app)       # '!'로 시작하는 명령어 추가


def addEMCommands(app):      # Commands startswith '!'
    @app.message(re.compile("^[!]"))
    def CommandWork(message, say):
        msg = AppMessage(message)   # 객체 변환

        if help.isHelpCommand(msg):   # Help 명령어 확인
            help.controlHelpCommand(msg, say)
        elif attendance.isAttendanceCommand(msg):   # Attendance 명령어 확인
            attendance.controlAttendanceCommand(msg, say)
        else:
            error.sayError(say, ERROR.INPUTERROR_TEXT)
