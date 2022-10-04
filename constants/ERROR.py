from constants.COMMAND import HELP, ATTENDANCE

ERROR_TAG = "error"
# 단순 에러체크를 위한 명령어 리스트
ERRORCHECK_LIST = HELP.COMMAND_LIST + ATTENDANCE.COMMAND_LIST

FORMATERROR_TEXT = "해당 명령어의 형식은 잘못된 형식입니다. 다시 확인하시고 입력바랍니다"
INPUTERROR_TEXT = "해당 명령어는 잘못된 명령어입니다. 다시 확인하시고 입력바랍니다"
SLEEPING_TEXT = "현재 취침시간(00:00~09:00)입니다. 잠시후 다시 시도해주세요."
