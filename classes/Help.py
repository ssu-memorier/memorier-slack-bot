from classes import Command
from constants.COMMAND import HELP, BASE


class Help(Command):     # 도움 커맨드
    def __init__(self, message, say):
        Command.__init__(self, message, say)

    def checkError(self):
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False
        return True if len(messageToken) == 1 else False

    def getHelpMessage(self):
        output = HELP.HELP_HEADLINE

        # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
        for identifier, commands in zip(BASE.COMMAND_IDENTIFIER_LIST, BASE.COMMAND_LIST):
            for command in commands:
                output += f"{identifier[command]} : {HELP.HELP_COMMAND_INFO[command]}\n"

        return output

    '''
        식별자와 커맨드명을 리턴해 주는 함수
    '''

    def getCommandName(command):
        return HELP.COMMAND_NAME[command]

    def getIdentifier(command):
        return HELP.COMMAND_IDENTIFIER[command]
