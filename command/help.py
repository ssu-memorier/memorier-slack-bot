from util.log import printCommandLogs
from constants import COMMAND, HELP       # 상수


def helpCommand(message, say):      # 도움
    helpOutput = HELP.HELP_HEADLINE

    for command in COMMAND.ATTENDANCE_COMMAND_LIST:
        helpOutput += f"{COMMAND.ATTENDANCE_COMMAND[command]} : {HELP.COMMAND_HELP_MESSAGE[command]}\n"

    # 서버에 log를 따로 남김
    printCommandLogs(message, COMMAND.ATTENDANCE_COMMAND[COMMAND.HELP])
    say(text=helpOutput, channel=message['channel'])
