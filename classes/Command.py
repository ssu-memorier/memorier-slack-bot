from constants import CHANNEL, ERROR

from utils import error, log


class Command():       # 기본 커맨드 클래스
    def __init__(self, message, say):
        self.command = self.__class__.__name__
        self.message = message
        self.say = say

        commandName = self.__class__.__name__
        self.commandName = self.getCommandName(commandName)
        self.identifier = self.getIdentifier(commandName)

    def checkError(self):
        if self.message.command not in ERROR.ERRORCHECK_LIST:
            return False
        else:
            return True

    def makeOutput(self):      # 커맨드 출력
        if self.checkError():
            output = ERROR.ERROR_TAG
        else:
            output = error.sayError(
                self.say, ERROR.FORMATERROR_TEXT)  # 명령어 형식 에러
        self.output = output

    def sayCommand(self):      # 커맨드 출력
        self.makeOutput()
        if self.output != ERROR.ERROR_TAG:
            self.sayToChannel(self.output)     # 채널에 출력
            log.printCommandLogs(self.message, self.command)    # 콘솔에 로그 출력

    def sayToChannel(self, text):      # 채널 출력
        self.say(text=text, channel=CHANNEL.BOT)

    '''
        식별자와 커맨드명을 리턴해 주는 함수
    '''

    def getCommandName(self):
        return None

    def getIdentifier(self):
        return None
