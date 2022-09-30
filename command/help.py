from utils.log import printCommandLogs
from constants.COMMAND import BASE, HELP      # 상수


def helpCommand():      # 도움
    helpOutput = HELP.HELP_HEADLINE

    # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
    for rgx, commands in zip(BASE.COMMAND_IDENTIFIER_LIST, BASE.COMMAND_LIST):
        for command in commands:
            helpOutput += f"{rgx[command]} : {HELP.HELP_COMMAND_INFO[command]}\n"

    return helpOutput, HELP.COMMAND_IDENTIFIER[HELP.COMMAND]


def errorCheckHelp(message):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
    messageToken = message.text.split()
    if messageToken[0] != HELP.COMMAND_IDENTIFIER[HELP.COMMAND]:    # 설마 명령어가 잘못되지는 않았겠지?
        return False
    return True if len(messageToken) == 1 else False
