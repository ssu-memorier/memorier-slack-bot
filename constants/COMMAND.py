CHANNEL_ATTENDANCE = '출석-체크'

# Command Keyword
HELP, GTW, LTW, OW, LATE = "help", "GoToWork", "LeaveToWork", "OfflineWork", "late"
OFFLINE = "!(오프|자리비움) \d"

COMMAND_IDENTIFY = "!"
ATTENDANCE_COMMAND_LIST = [HELP, GTW, LTW, OW]  # Command list
ATTENDANCE_COMMAND_NAME = {        # Command name
    HELP: "도움",
    GTW: "출근",
    LTW: "퇴근",
    OW: "자리비움(오프)",
    LATE: "지각"
}
ATTENDANCE_COMMAND = {        # Command Keyword
    HELP: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[HELP],     # "!도움"
    GTW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[GTW],       # "!출근"
    LTW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[LTW],       # "!퇴근"
    OW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[OW],         # "!자리비움(오프)"
    LATE: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[LATE]      # "!지각"
}
