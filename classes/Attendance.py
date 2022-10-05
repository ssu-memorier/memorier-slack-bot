from constants import CHANNEL
from constants.COMMAND import ATTENDANCE
from classes.Command import Command

from constants import ERROR
from utils import error


class Attendance(Command):     # 출석 커맨드
    def __init__(self, message, say):
        Command.__init__(self, message, say)
        # self.output = ""

    def sayToChannel(self, text):  # 채널에 메세지 출력
        self.say(text=text, channel=CHANNEL.ATTENDANCE)

    def getAttendanceMessage(self):      # 출력할 텍스트
       # date : Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)
        if self.command == ATTENDANCE.OW:  # 자리비움의 경우 시간까지 입력
            # tokens = [커맨드(자리비움), 시간]
            [_, offTime] = self.message.text.split()

            return f"[ <@{self.message.userID}> ] {self.message.date}\t{offTime}시간 {ATTENDANCE.COMMAND_NAME[self.command]}"
        else:
            return f"[ <@{self.message.userID}> ] {self.message.date}\t{ATTENDANCE.COMMAND_NAME[self.command]}"

    def makeOutput(self):
        if self.checkError():     # 에러 체크 진행
            output = self.getAttendanceMessage()
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러

        return output

    '''
        식별자와 커맨드명을 리턴해 주는 함수
    '''

    def getCommandName(self, command):
        return ATTENDANCE.COMMAND_NAME[command]

    def getIdentifier(self, command):
        return ATTENDANCE.COMMAND_IDENTIFIER[command]
