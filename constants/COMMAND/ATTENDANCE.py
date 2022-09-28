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
    # "!자리비움(오프)"
    OW: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[OW],
    LATE: COMMAND_IDENTIFY + ATTENDANCE_COMMAND_NAME[LATE]      # "!지각"
}
