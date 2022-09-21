# -*- coding: utf-8 -*-

# Module Function
from util.utils import getCurrentSeoulTime, getSlackToken
from command.help import helpCommand
from constants.constants import *       # 상수

# Python Libraries
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# get Token
slackAppToken, slackBotToken = getSlackToken()

# 앱 실행
app = App(token=slackBotToken)
    
# !도움말
@app.message(re.compile((HELP)))
def say_comment_help(message, say):
    helpCommand(message, say)

# 메인 진행 함수
def main():
    SocketModeHandler(app, slackAppToken).start()

# main 실행문
if __name__ == "__main__":
    main()
    