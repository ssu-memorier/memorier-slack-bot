from classes import Attendance
from constants.COMMAND import IDENTIFIER


class OfflineWork(Attendance):  # !오프 (시간)
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def checkError(self):    # OfflineWork 명령어가 제대로 들어왔는지 확인
        # 자리비움 예약 미구현 상태
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False

        return True if (len(messageToken) == 2) and (messageToken[IDENTIFIER.SUBARGS_INDEX].isdigit()) else False
