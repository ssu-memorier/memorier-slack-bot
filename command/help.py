from constants.COMMAND import BASE, HELP, IDENTIFIER      # 상수
from command.commands import Commands


class Help(Commands):     # 도움 커맨드
    def __init__(self, message, say):
        Commands.__init__(self, message, say)

    def errorCheck(self):
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != HELP.COMMAND_IDENTIFIER[HELP.COMMAND]:
            return False
        return True if len(messageToken) == 1 else False

    def getTextForChannel(self):
        output = HELP.HELP_HEADLINE

        # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
        for identifier, commands in zip(BASE.COMMAND_IDENTIFIER_LIST, BASE.COMMAND_LIST):
            for command in commands:
                output += f"{identifier[command]} : {HELP.HELP_COMMAND_INFO[command]}\n"

        return output


'''
    커맨드 체크 명령어 : manageCommand에서 커맨드 분류에 사용
'''


def isHelpCommand(message):  # help 명령어인지 확인하는 함수
    # help 명령어 인지 확인
    return True if message.text.startswith(IDENTIFIER.HELP) else False


def controlHelpCommand(message, say):      # 도움 관련 명령어 제어문
    works = Help(message, say)
    works.sayCommand()      # 커맨드 출력
