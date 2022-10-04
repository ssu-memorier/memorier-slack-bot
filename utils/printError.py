from constants import CHANNEL, ERROR


def commandFormatError(say):       # 명령어 형식 에러
    printText = ERROR.FORMATERROR_TEXT
    say(text=printText, channel=CHANNEL.BOT)


def commandInputError(say):    # 명령어 실행 에러
    printText = ERROR.INPUTERROR_TEXT
    say(text=printText, channel=CHANNEL.BOT)
