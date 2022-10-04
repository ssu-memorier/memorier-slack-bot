from constants import CHANNEL, ERROR
from constants.COMMAND import ATTENDANCE, IDENTIFIER

from utils import error, log, date


class AppMessage():     # app으로 부터 받은 메시지 정보를 관리하는 클래스
    def __init__(self, message):
        self.channel = message['channel']
        self.text = message['text']
        self.userID = message['user']
        self.command = message['text'].split()[IDENTIFIER.COMMAND_INDEX]

        # 명령어가 실행된 날짜값 저장
        self.ts = message['ts']     # timestamp
        self.date = date.ts2datetime(float(message['ts']))      # datetime
        self.hour, self.minute = date.getTs2HourMinute(
            float(message['ts']))    # HH, MM


class Commands():       # 기본 커맨드 클래스
    def __init__(self, message, say):
        self.command = self.__class__.__name__
        self.message = message
        self.say = say

    def errorCheck(self):
        if self.message.command not in ERROR.ERRORCHECK_LIST:
            return False
        else:
            return True

    def sayCommand(self):      # 커맨드 출력
        if self.errorCheck():
            output = self.getTextForChannel()
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러

        if output != ERROR.ERROR_TAG:
            self.sayToChannel(output)     # 채널에 출력
            log.printCommandLogs(self.message, self.command)    # 콘솔에 로그 출력

    def getTextForChannel(self):      # 출력할 텍스트
        # date : Command가 실행된 날짜데이터(YY-MM-DD HH:MM:SS)
        if self.command == ATTENDANCE.OW:  # 자리비움의 경우 시간까지 입력
            # tokens = [커맨드(자리비움), 시간]
            [_, offTime] = self.message.text.split()

            return f"[ <@{self.message.userID}> ] {self.message.date}\t{offTime}시간 {ATTENDANCE.COMMAND_NAME[self.command]}"
        else:
            return f"[ <@{self.message.userID}> ] {self.message.date}\t{ATTENDANCE.COMMAND_NAME[self.command]}"

    def sayToChannel(self, text):      # 채널 출력
        self.say(text=text, channel=CHANNEL.BOT)
