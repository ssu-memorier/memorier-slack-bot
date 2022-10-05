from constants.COMMAND import ATTENDANCE, IDENTIFIER

# Help Command
COMMAND = "Help"

COMMAND_NAME = {        # Command name list
    COMMAND: "도움"
}

COMMAND_LIST = [COMMAND]  # Command list
COMMAND_IDENTIFIER = {        # Command Identifier
    COMMAND: IDENTIFIER.COMMAND + COMMAND_NAME[COMMAND]     # !도움
}
HELP_COMMAND_INFO = {        # !help command infomations
    ATTENDANCE.GTW: "현재시간으로 출근 처리가 진행됩니다.",
    ATTENDANCE.LTW: "현재시간으로 퇴근 처리가 진행됩니다.",
    ATTENDANCE.OW: "현재시간부터 해당 시간만큼 오프 처리됩니다. (예약기능 포함)",
    COMMAND: "실행 가능한 전체 명령어에 대해 알려줍니다."
}

HELP_HEADLINE = "\n< 명령어 도움말 >\n"  # !도움 Output Constants
