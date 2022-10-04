from utils.log import printCommandLogs
from constants.COMMAND import BASE, HELP, IDENTIFIER      # 상수


def helpCommand():      # 도움
    helpOutput = HELP.HELP_HEADLINE

    # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
    for identifier, commands in zip(BASE.COMMAND_IDENTIFIER_LIST, BASE.COMMAND_LIST):
        for command in commands:
            helpOutput += f"{identifier[command]} : {HELP.HELP_COMMAND_INFO[command]}\n"

    return helpOutput, HELP.COMMAND_IDENTIFIER[HELP.COMMAND]


def helpErrorCheck(message):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
    messageToken = message.text.split()
    # 설마 명령어가 잘못되지는 않았겠지?
    if messageToken[IDENTIFIER.COMMAND_INDEX] != HELP.COMMAND_IDENTIFIER[HELP.COMMAND]:
        return False
    return True if len(messageToken) == 1 else False
