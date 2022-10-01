from command import help, attendance      # help, 출석 관련 명령어
from utils import printError
from constants.COMMAND import BASE


def Gotowork(message, say):     # !출근 명령어
    if attendance.errorCheckGoToWork(message):
        attendanceOutput, command = attendance.goToWork(message)
    else:
        printError.commandFormatError(say)  # 명령어 형식 에러
        return None, BASE.ERROR       # 에러 리턴
    return attendanceOutput, command


def Leavetowork(message, say):     # !퇴근 명령어
    if attendance.errorCheckLeaveToWork(message):
        attendanceOutput, command = attendance.leaveToWork(message)
    else:
        printError.commandFormatError(say)  # 명령어 형식 에러
        return None, BASE.ERROR       # 에러 리턴
    return attendanceOutput, command


def Offline(message, say):     # !오프 명령어
    if attendance.errorCheckOfflineWork(message):
        attendanceOutput, command = attendance.offlineWork(message)
    else:
        printError.commandFormatError(say)  # 명령어 형식 에러
        return None, BASE.ERROR       # 에러 리턴
    return attendanceOutput, command


def Help(message, say):     # !도움 명령어
    if help.errorCheckHelp(message):
        helpOutput, command = help.helpCommand()
    else:
        printError.commandFormatError(say)  # 명령어 형식 에러
        return None, BASE.ERROR       # 에러 리턴
    return helpOutput, command
