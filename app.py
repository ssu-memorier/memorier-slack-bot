# -*- coding: utf-8 -*-
from module.utils import getCurrentSeoulTime, getSlackToken
from module.attendance import GoToWork, LeaveToWork, OfflineWork

import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# get Token
slackAppToken, slackBotToken = getSlackToken()

# 앱 실행
app = App(token=slackBotToken)
    
# !출근
@app.message(re.compile("(!출근)"))
def say_comment_gotowork(message, say):
    GoToWork(message, say)

# !퇴근
@app.message(re.compile(("!퇴근")))
def say_comment_leavetowork(message, say):
    LeaveToWork(message, say)

# !오프 (시간)
@app.message(re.compile("(!오프) \d"))
def say_comment_off(message, say):
    OfflineWork(message, say)

# 메인 진행 함수
def main():
    print("="*10,"SlackBot is started","="*10,'\n'*2)       # slackbot 시작
    SocketModeHandler(app, slackAppToken).start()

# main 실행문
if __name__ == "__main__":
    main()