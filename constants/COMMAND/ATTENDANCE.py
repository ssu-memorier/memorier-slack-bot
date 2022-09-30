from constants.COMMAND import IDENTIFIER
# Attendance Command
GTW, LTW, OW, LATE = "GoToWork", "LeaveToWork", "OfflineWork", "late"
GOTOWORK_REG = "!출근"
LEAVETOWORK_REG = "!퇴근"
OFFLINE_REG = "!(오프|자리비움) \d"

COMMAND_LIST = [GTW, LTW, OW]  # Command list
COMMAND_NAME = {        # Command name list
    GTW: "출근",
    LTW: "퇴근",
    OW: "자리비움(오프)",
    LATE: "지각"
}
COMMAND_REGEX = {        # Command Keyword
    GTW: IDENTIFIER.COMMAND + COMMAND_NAME[GTW],       # "!출근"
    LTW: IDENTIFIER.COMMAND + COMMAND_NAME[LTW],       # "!퇴근"
    OW: IDENTIFIER.COMMAND + COMMAND_NAME[OW],         # "!자리비움(오프)"
    LATE: IDENTIFIER.COMMAND + COMMAND_NAME[LATE]      # "!지각"
}
