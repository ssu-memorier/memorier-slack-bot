import re       # 정규식

from constants.COMMAND import HELP, ATTENDANCE
from utils import date
from utils.log import sayHelpChannel, sayAttendanceChannel
from command import help, attendance      # help, 출석 관련 명령어


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


def addHelpCommand(app):      # 도움말 관련 명령어 추가
    # !도움말
    @app.message(re.compile(HELP.HELP_REG))
    def sayCommentHelp(message, say):
        helpOutput = help.helpCommand(AppMessage(message), say)
        sayHelpChannel(say, helpOutput)


def addAttendanceCommand(app):      # 출석 관련 명령어 추가

    @app.message(re.compile(ATTENDANCE.GOTOWORK_REG))  # !출근
    def sayCommentGotowork(message, say):
        attendanceOutput = attendance.goToWork(AppMessage(message), say)
        sayAttendanceChannel(say, attendanceOutput)

    @app.message(re.compile(ATTENDANCE.LEAVETOWORK_REG))  # !퇴근
    def sayCommentLeavetowork(message, say):
        attendanceOutput = attendance.leaveToWork(AppMessage(message), say)
        sayAttendanceChannel(say, attendanceOutput)

    @app.message(re.compile(ATTENDANCE.OFFLINE_REG))  # !오프 (시간)
    def sayCommentOff(message, say):
        attendanceOutput = attendance.offlineWork(AppMessage(message), say)
        sayAttendanceChannel(say, attendanceOutput)


def addAllCommands(app):        # 모든 Command가 실행되도록 추가
    addHelpCommand(app)
    addAttendanceCommand(app)
