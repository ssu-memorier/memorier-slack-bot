from utils.log import printCommandLogs
from constants import COMMAND       # 상수


def helpCommand(message, say):      # 도움
    helpOutput = COMMAND.HELP_HEADLINE

    # 출력할 명령어 목록 전처리 작업 진행
    commandList = []
    for rgx, commands in zip(COMMAND.COMMAND_REG_LIST, COMMAND.COMMAND_LIST):
        commandList.append([rgx, commands])

    # 출력할 리스트에서 하나씩 "명령어 : 도움말" 형식으로 출력 진행
    for commandInfo in commandList:
        [commandReg, commands] = commandInfo
        for command in commands:
            helpOutput += f"{commandReg[command]} : {COMMAND.HELP_COMMAND_INFO[command]}\n"

    # 서버에 log를 따로 남김
    printCommandLogs(message, COMMAND.HELP_COMMAND_REGEX[COMMAND.HELP])
    say(text=helpOutput, channel=message.channel)
