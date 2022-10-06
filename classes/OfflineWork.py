from classes.Attendance import Attendance
from constants.COMMAND import ATTENDANCE

from constants import ERROR, DATE
from utils import error


class OfflineWork(Attendance):  # !오프 (시간)
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def checkError(self):    # OfflineWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False

        if len(messageToken) == 2:  # !오프 (숫자) : 일반적인 오프
            if messageToken[ATTENDANCE.OFFLINE_TIME_INDEX].isdigit():
                return True
        elif len(messageToken) == 3:    # !오프 (숫자) (숫자) : 오프 예약
            if messageToken[ATTENDANCE.OFFLINE_TIME_INDEX].isdigit() and \
                    messageToken[ATTENDANCE.OFFLINE_STARTTIME_INDEX].isdigit():
                return True
        else:
            return False

    def makeOutput(self):
        if self.isNotAvailableOffTime():
            output = error.sayError(
                self.say, ERROR.TIMEFORMAT_TEXT)  # 시간 입력 형식 에러
        elif self.checkError():     # 에러 체크 진행
            output = self.getAttendanceMessage()
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러

        return output

    def getAttendanceMessage(self):      # 출력할 텍스트
       # date : Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)
        if self.command == ATTENDANCE.OW:  # 자리비움의 경우 시간까지 입력
            messageToken = self.message.text.split()
            if len(messageToken) == 2:  # !오프 (시간) : 실시간 오프
                # tokens = [커맨드(자리비움), 시간]
                [_, offTime] = self.message.text.split()

                return f"[ <@{self.message.userID}> ] {self.message.date}\t{offTime}시간 {ATTENDANCE.COMMAND_NAME[self.command]}"
            else:   # !오프 (예약시간) (시간):오프 예약
                [_, offTime, reserveTime] = self.message.text.split()
                return f"[ <@{self.message.userID}> ] {self.message.date}\t{reserveTime}부터 {offTime}시간 {ATTENDANCE.COMMAND_NAME[self.command]} 예약"
        else:
            return f"[ <@{self.message.userID}> ] {self.message.date}\t{ATTENDANCE.COMMAND_NAME[self.command]}"

    def isNotAvailableOffTime(self):   # 오프시간이 근무시간(8시간) 초과인 경우 에러
        messageToken = self.message.text.split()
        if not messageToken[ATTENDANCE.OFFLINE_TIME_INDEX].isdigit():
            return True
        elif int(messageToken[ATTENDANCE.OFFLINE_TIME_INDEX]) > DATE.WORKINGHOUR or \
                int(messageToken[ATTENDANCE.OFFLINE_TIME_INDEX]) <= 0:
            return True
        else:
            return False
