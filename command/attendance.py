from constants import DATE, CHANNEL, ERROR
from constants.COMMAND import ATTENDANCE, IDENTIFIER     # 상수

from command.commands import Commands
from utils import date, error, log


class Attendance(Commands):     # 출석 커맨드
    def __init__(self, message, say):
        Commands.__init__(self, message, say)

    def sayToChannel(self, text):  # 채널에 메세지 출력
        self.say(text=text, channel=CHANNEL.ATTENDANCE)


''' 
    세부 명령어 : !출근, !퇴근, !오프
'''


class GoToWork(Attendance):  # !출근
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def errorCheck(self):    # GoToWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()

        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.GTW]:
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
        elif self.errorCheck():     # 에러 체크 진행
            output = self.getTextForChannel()
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러

        if output != ERROR.ERROR_TAG:
            self.sayToChannel(output)     # 채널에 출력
            log.printCommandLogs(self.message, self.command)    # 콘솔에 로그 출력

    def getTextForChannel(self):
        self.isLate()       # 지각인지 확인
        return super().getTextForChannel()


class LeaveToWork(Attendance):  # !퇴근
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def errorCheck(self):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.LTW]:
            return False
        return True if len(messageToken) == 1 else False


class OfflineWork(Attendance):  # !오프 (시간)
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def errorCheck(self):    # OfflineWork 명령어가 제대로 들어왔는지 확인
        # 자리비움 예약 미구현 상태
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.OW]:
            return False

        return True if (len(messageToken) == 2) and (messageToken[IDENTIFIER.SUBARGS_INDEX].isdigit()) else False


'''
    커맨드 체크 명령어 : manageCommand에서 커맨드 분류에 사용
'''


def isAttendanceCommand(message):   # Attendance 명령어인지 확인하는 함수
    # Attendance 명령어 리스트를 하나씩 확인하며 해당 명령어가 있는지 확인
    for identifier in IDENTIFIER.ATTENDANCE:
        if message.text.startswith(identifier):
            return True
    else:
        return False


def controlAttendanceCommand(message, say):      # 출석 관련 명령어 제어문
    if message.text.startswith(IDENTIFIER.GOTOWORK):    # !출근
        works = GoToWork(message, say)
    elif message.text.startswith(IDENTIFIER.LEAVETOWORK):  # !퇴근
        works = LeaveToWork(message, say)
    elif message.text.startswith(IDENTIFIER.OFFLINE):   # !오프
        works = OfflineWork(message, say)

    works.sayCommand()      # 커맨드 출력
