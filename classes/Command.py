from constants import CHANNEL, ERROR

from utils import error, log


class Command():       # 기본 커맨드 클래스
    def __init__(self, message, say):
        self.command = self.__class__.__name__
        self.message = message
        self.say = say
        command = self.__class__.__name__
        self.commandName = self.getCommandName(command)
        self.identifier = self.getIdentifier(command)

    def checkError(self):
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

    def sayToChannel(self, text):      # 채널 출력
        self.say(text=text, channel=CHANNEL.BOT)

    '''
        식별자와 커맨드명을 리턴해 주는 함수
    '''

    def getCommandName(command):
        return None

    def getIdentifier(command):
        return None
