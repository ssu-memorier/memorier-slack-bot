from constants import DATE
from constants.COMMAND import ATTENDANCE, IDENTIFIER     # 상수

from utils import log, date

''' 명령어 실행문 '''


def goToWork(message):  # !출근
    # 10시 10분 넘어서 출근을 하면 지각 처리
    if date.isTimeInBetween(message.ts, DATE.ATTENDANCE_TIME):
        state = ATTENDANCE.GTW
    else:
        state = ATTENDANCE.LATE

    outputText = log.printWorkState(message, state)   # 채널 출력문 생성
    return outputText, ATTENDANCE.COMMAND_NAME[state]


def leaveToWork(message):  # !퇴근
    outputText = log.printWorkState(message, ATTENDANCE.LTW)   # 채널 출력문 생성
    return outputText, ATTENDANCE.COMMAND_NAME[ATTENDANCE.LTW]


def offlineWork(message):  # !오프 (시간)
    outputText = log.printWorkState(message, ATTENDANCE.OW)   # 채널 출력문 생성
    return outputText, ATTENDANCE.COMMAND_NAME[ATTENDANCE.OW]


''' 명령어 에러 체크 '''


def goToWorkErrorCheck(message):    # GoToWork 명령어가 제대로 들어왔는지 확인
    messageToken = message.text.split()
    # 설마 명령어가 잘못되지는 않았겠지?
    if messageToken[IDENTIFIER.COMMAND_INDEX] != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.GTW]:
        return False
    return True if len(messageToken) == 1 else False


def leaveToWorkErrorCheck(message):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
    messageToken = message.text.split()
    # 설마 명령어가 잘못되지는 않았겠지?
    if messageToken[IDENTIFIER.COMMAND_INDEX] != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.LTW]:
        return False
    return True if len(messageToken) == 1 else False


def offlineWorkErrorCheck(message):    # OfflineWork 명령어가 제대로 들어왔는지 확인
    # 자리비움 예약 미구현 상태
    messageToken = message.text.split()
    # 설마 명령어가 잘못되지는 않았겠지?
    if messageToken[IDENTIFIER.COMMAND_INDEX] != ATTENDANCE.COMMAND_IDENTIFIER[ATTENDANCE.OW]:
        return False
    return True if (len(messageToken) == 2) and (messageToken[IDENTIFIER.SUBARGS_INDEX].isdigit()) else False
