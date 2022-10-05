from constants.COMMAND import IDENTIFIER      # 상수
from classes import Help


'''
    커맨드 체크 명령어 : manageCommand에서 커맨드 분류에 사용
'''


def isHelpCommand(message):  # help 명령어인지 확인하는 함수
    # help 명령어 인지 확인
    return True if message.text.startswith(IDENTIFIER.HELP) else False


def controlHelpCommand(message, say):      # 도움 관련 명령어 제어문
    works = Help(message, say)
    works.sayCommand()      # 커맨드 출력
