from utils.log import printCommandLogs
from constants.COMMAND import BASE, HELP      # 상수


def helpCommand(message):      # 도움
    helpOutput = HELP.HELP_HEADLINE

    # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
    for rgx, commands in zip(BASE.COMMAND_REG_LIST, BASE.COMMAND_LIST):
        for command in commands:
            helpOutput += f"{rgx[command]} : {HELP.HELP_COMMAND_INFO[command]}\n"

    # 서버에 log를 따로 남김
    printCommandLogs(message, HELP.COMMAND_IDENTIFIER[HELP.COMMAND_NAME])
    return helpOutput
