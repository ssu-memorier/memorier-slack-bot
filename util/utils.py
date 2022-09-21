# get Time
from datetime import datetime
from pytz import timezone
from constants.constants import *

# functions
def getCurrentSeoulTime():
    return datetime.now(timezone(ASIA_SEOUL))

def printCommandLogs(message, command):
    user = message['user']
    currentTime = getCurrentSeoulTime().strftime(DATE_FORMAT)
    print(f"{currentTime}\t{user}가 {command} 명령어를 사용하였습니다")
    