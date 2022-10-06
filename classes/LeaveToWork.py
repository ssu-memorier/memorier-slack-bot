from classes.Attendance import Attendance
from constants import DATE, ERROR
from utils import date, error


class LeaveToWork(Attendance):  # !퇴근
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def checkError(self):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False
        return True if len(messageToken) == 1 else False

    def makeOutput(self):      # 코어타임 확인 추가
        if date.isTimeInBetween(self.message.ts, DATE.CORE_TIME):
            output = error.sayError(
                self.say, ERROR.CANT_USE_COMMAND_IN_CORETIME)  # 코어타임 해당 명령어 사용 금지
        elif self.checkError():     # 에러 체크 진행
            output = self.getAttendanceMessage()
        else:
            output = error.sayError(
                self.say, ERROR.FORMAT_ERROR)  # 명령어 형식 에러

        return output
