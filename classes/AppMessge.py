from constants.COMMAND import IDENTIFIER

from utils import date


class AppMessage():     # app으로 부터 받은 메시지 정보를 관리하는 클래스
    def __init__(self, message):
        self.channel = message['channel']
        self.text = message['text']
        self.userID = message['user']
        self.command = message['text'].split()[IDENTIFIER.COMMAND_INDEX]

        # 명령어가 실행된 날짜값 저장
        self.ts = message['ts']     # timestamp
        self.date = date.ts2datetime(float(message['ts']))      # datetime
        self.hour, self.minute = date.getTs2HourMinute(
            float(message['ts']))    # HH, MM
