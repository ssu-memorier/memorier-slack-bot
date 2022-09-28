CHANNEL_ATTENDANCE = '출석-테스트'
COMMAND_IDENTIFY = "!"

# Attendance Command
GTW, LTW, OW, LATE = "GoToWork", "LeaveToWork", "OfflineWork", "late"
GOTOWORK_REG = "!출근"
LEAVETOWORK_REG = "!퇴근"
OFFLINE_REG = "!(오프|자리비움) \d"

ATTENDANCE_COMMAND_LIST = [GTW, LTW, OW]  # Command list
ATTENDANCE_COMMAND_NAME = {        # Command name
    GTW: "출근",
    LTW: "퇴근",
    OW: "자리비움(오프)",
    LATE: "지각"
}
ATTENDANCE_COMMAND_REGEX = {        # Command Keyword
    GTW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[GTW],       # "!출근"
    LTW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[LTW],       # "!퇴근"
    OW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[OW],         # "!자리비움(오프)"
    LATE: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[LATE]      # "!지각"
}


# Help Command
HELP = "help"
HELP_REG = "!도움"

HELP_COMMAND_LIST = [HELP]  # Command list
HELP_COMMAND_REGEX = {
    HELP: COMMAND_IDENTIFY + HELP
}
HELP_COMMAND_INFO = {        # !help command infomations
    GTW: "현재시간으로 출근 처리가 진행됩니다.",
    LTW: "현재시간으로 퇴근 처리가 진행됩니다.",
    OW: "현재시간부터 해당 시간만큼 자리비움(오프) 상태로 처리됩니다.",
    HELP: "실행가능한 전체 명령어에 대해 나오게 됩니다."
}

HELP_HEADLINE = "\n< 명령어 도움말 >\n"  # !도움 Output Constants


# 전체 Command 리스트
COMMAND_LIST = [HELP_COMMAND_LIST, ATTENDANCE_COMMAND_LIST]
COMMAND_REG_LIST = [ATTENDANCE_COMMAND_REGEX, HELP_COMMAND_REGEX]
