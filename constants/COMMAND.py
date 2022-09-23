CHANNEL_ATTENDANCE = '출석-테스트'

# Command Keyword
HELP, GTW, LTW, OW, LATE = "help", "GoToWork", "LeaveToWork", "OfflineWork", "late"
OFFLINE = "!(오프|자리비움) \d"

ATTENDANCE_COMMAND_LIST = [HELP, GTW, LTW, OW]  # Command list
ATTENDANCE_COMMAND = {        # Command Keyword
    HELP: "!도움",
    GTW: "!출근",
    LTW: "!퇴근",
    OW: "!자리비움(오프)",
    LATE: "!지각"
}
