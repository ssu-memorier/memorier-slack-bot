from constants import CHANNEL, ERROR


def sayError(say, text):
    # ERROR.FORMATERROR_TEXT : 명령어 형식 에러
    # ERROR.INPUTERROR_TEXT : 명령어 실행 에러
    say(text=text, channel=CHANNEL.BOT)
    return ERROR.ERROR_TAG
