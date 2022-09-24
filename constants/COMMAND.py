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

# MESSAGE TOKEN에서 값을 나타내는 인덱스
MESSAGE_TOKEN_COMMAND = 0
MESSAGE_TOKEN_TIME = 1

# 코어타임 관련 Log, Output TEXT 목록
CORETIME_LOG = {
    LTW: "Error log\tCore Time에 !퇴근을 시도하였습니다.",
    OW: "Error log\tCore Time에 !오프를 시도하였습니다."
}
CORETIME_OUTPUT = {
    LTW: ":warning:\t현재는 Core Time (20:00:00~23:00:00) 으로 퇴근 하실 수 없습니다.",
    OW: ":warning:\t현재는 Core Time (20:00:00~23:00:00) 으로 오프 하실 수 없습니다."
}
