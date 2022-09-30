from constants.COMMAND import CHANNEL


def commandFormatError(say):       # 명령어 형식 에러
    printText = "해당 명령어의 형식은 잘못된 형식입니다. 다시 확인하시고 입력바랍니다"
    say(text=printText, channel=CHANNEL.BOT)


def commandExecutionError(say):    # 명령어 실행 에러
    printText = "해당 명령어는 잘못된 명령어입니다. 다시 확인하시고 입력바랍니다"
    say(text=printText, channel=CHANNEL.BOT)
