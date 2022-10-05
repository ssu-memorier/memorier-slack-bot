from constants.COMMAND import ATTENDANCE
from constants import DATE, ERROR

from utils import date, error, log
from classes import Attendance


class GoToWork(Attendance):  # !출근
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def checkError(self):    # GoToWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()

        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False
        return True if len(messageToken) == 1 else False

    def isLate(self):
        # 10시 10분 넘어서 출근을 하면 지각 처리
        if date.isTimeInBetween(self.message.ts, DATE.ATTENDANCE_TIME):
            self.command = ATTENDANCE.GTW
        else:
            self.command = ATTENDANCE.LATE

    def sayCommand(self):      # 취침시간 확인 추가
        if date.isTimeInBetween(self.message.ts, DATE.SLEEPING_TIME):
            output = error.sayError(
                self.say, ERROR.SLEEPING_TEXT)  # 취침시간
        elif self.checkError():     # 에러 체크 진행
            output = self.getTextForChannel()
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러

        if output != ERROR.ERROR_TAG:
            self.sayToChannel(output)     # 채널에 출력
            log.printCommandLogs(self.message, self.command)    # 콘솔에 로그 출력

    def getAttendanceMessage(self):
        self.isLate()       # 지각인지 확인
        return super().getAttendanceMessage()
