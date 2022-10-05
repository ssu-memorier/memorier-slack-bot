from classes import GoToWork, LeaveToWork, OfflineWork

from constants.COMMAND import IDENTIFIER     # 상수

'''
    커맨드 체크 명령어 : manageCommand 에서 커맨드 분류에 사용
'''


def isAttendanceCommand(message):   # Attendance 명령어인지 확인하는 함수
    # Attendance 명령어 리스트를 하나씩 확인하며 해당 명령어가 있는지 확인
    for identifier in IDENTIFIER.ATTENDANCE:
        if message.text.startswith(identifier):
            return True
    else:
        return False


def controlAttendanceCommand(message, say):      # 출석 관련 명령어 제어문
    if message.text.startswith(IDENTIFIER.GOTOWORK):    # !출근
        works = GoToWork(message, say)
    elif message.text.startswith(IDENTIFIER.LEAVETOWORK):  # !퇴근
        works = LeaveToWork(message, say)
    elif message.text.startswith(IDENTIFIER.OFFLINE):   # !오프
        works = OfflineWork(message, say)

    works.sayCommand()      # 커맨드 출력
