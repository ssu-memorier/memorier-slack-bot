from constants.COMMAND import IDENTIFIER
# Attendance Command
GTW, LTW, OW, LATE = "GoToWork", "LeaveToWork", "OfflineWork", "late"

COMMAND_NAME = {        # Command name list
    GTW: "출근",
    LTW: "퇴근",
    OW: "오프",
    LATE: "지각"
}
COMMAND_LIST = [GTW, LTW, OW]  # Command list
COMMAND_IDENTIFIER = {        # Command Identifier
    GTW: IDENTIFIER.COMMAND + COMMAND_NAME[GTW],       # "!출근"
    LTW: IDENTIFIER.COMMAND + COMMAND_NAME[LTW],       # "!퇴근"
    OW: IDENTIFIER.COMMAND + COMMAND_NAME[OW],         # "!오프"
    LATE: IDENTIFIER.COMMAND + COMMAND_NAME[LATE]      # "!지각"
}
