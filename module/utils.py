# get Time
from datetime import datetime
from pytz import timezone

# token
import json

# Common Variables
tokenLink = 'assets/slack_token.json'
READ_MODE = 'r'

# functions
def getCurrentSeoulTime():
    return datetime.now(timezone('Asia/Seoul'))

def getSlackToken():
    # go to Keys and get dictionary
    with open(tokenLink, READ_MODE) as f:
        keys = json.load(f)
        
    # get Token
    slack_bot_token = keys['slack_token']['slack_bot_token']
    slack_app_token = keys['slack_token']['slack_app_token']
    return slack_app_token, slack_bot_token

def printCommandLogs(message, command):
    user = message['user']
    currnetTime = getCurrentSeoulTime().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{currnetTime}\t{user}가 {command} 명령어를 사용하였습니다")