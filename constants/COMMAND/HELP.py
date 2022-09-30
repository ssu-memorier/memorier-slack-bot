from constants.COMMAND import ATTENDANCE, IDENTIFIER

# Help Command
COMMAND_NAME = "help"

COMMAND_LIST = [COMMAND_NAME]  # Command list
COMMAND_IDENTIFIER = IDENTIFIER.COMMAND + COMMAND_NAME
HELP_COMMAND_INFO = {        # !help command infomations
    ATTENDANCE.GTW: "현재시간으로 출근 처리가 진행됩니다.",
    ATTENDANCE.LTW: "현재시간으로 퇴근 처리가 진행됩니다.",
    ATTENDANCE.OW: "현재시간부터 해당 시간만큼 자리비움(오프) 상태로 처리됩니다.",
    COMMAND_NAME: "실행가능한 전체 명령어에 대해 나오게 됩니다."
}

HELP_HEADLINE = "\n< 명령어 도움말 >\n"  # !도움 Output Constants
