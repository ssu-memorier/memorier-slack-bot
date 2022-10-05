from classes.Attendance import Attendance


class LeaveToWork(Attendance):  # !퇴근
    def __init__(self, message, say):
        Attendance.__init__(self, message, say)

    def checkError(self):    # LeaveToWork 명령어가 제대로 들어왔는지 확인
        messageToken = self.message.text.split()
        # 설마 명령어가 잘못되지는 않았겠지?
        if self.message.command != self.identifier:
            return False
        return True if len(messageToken) == 1 else False
