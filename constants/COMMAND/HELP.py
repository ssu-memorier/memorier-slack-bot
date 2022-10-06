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
    ATTENDANCE.GTW: """현재시간으로 출근 처리가 진행됩니다. 출근시간 이후로 출근할 경우 지각처리 됩니다. (취침시간에는 출근할 수 없습니다.)
    예) !출근""",
    ATTENDANCE.LTW: """현재시간으로 퇴근 처리가 진행됩니다. (코어타임에는 퇴근 할 수 없습니다.)
    예) !퇴근""",
    ATTENDANCE.OW: """현재시간 또는 예약시간부터 해당 시간만큼 오프 처리됩니다. (코어타임에는 오프 할 수 없습니다.)
    예) !오프 4 (4시간 자리비움) or !오프 4 1200 (1200부터 4시간 자리비움 예약)""",
    COMMAND: """실행 가능한 전체 명령어에 대해 알려줍니다.
    예) !도움"""
}

HELP_HEADLINE = "\n< 명령어 도움말 >\n"  # !도움 Output Constants
