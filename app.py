# -*- coding: utf-8 -*-
from datetime import datetime
import json
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Key값 가져오기
with open("slack_token.json", "r") as f:
    slack = json.load(f)
    
# 토큰 부여
slack_bot_token = slack['slack']['slack_bot_token']
slack_app_token = slack['slack']['slack_app_token']

# 앱 실행
app = App(token=slack_bot_token)

# !출근
@app.message(re.compile("(!출근)"))
def say_comment_comein(message, say):
    date = datetime.now()       #현재시간
    print_comein = f"현재 <@{message['user']}> 가 {date.strftime('%Y-%m-%d %H:%M:%S')}에 출근하였습니다."
    
    say(text=print_comein, channel = '출석-체크')

# !퇴근
@app.message(re.compile(("!퇴근")))
def say_comment_comeout(message, say):
    date = datetime.now()       #현재시간
    print_comein = f"현재 <@{message['user']}> 가 {date.strftime('%Y-%m-%d %H:%M:%S')}에 퇴근하였습니다."
    
    say(text=print_comein, channel = '출석-체크')

# !자리비움 (시간)
@app.message(re.compile("(!자리비움) \d"))
def say_comment_off(message, say):
    date = datetime.now()       #현재시간
    duringTime = message['text'].split()[1]
    print_comein = f"현재 <@{message['user']}> 가 {date.strftime('%Y-%m-%d %H:%M:%S')}부터 {duringTime}시간동안 자리를 비울 예정입니다."
    
    say(text=print_comein, channel = '출석-체크')
    
# !도움말
@app.message(re.compile(("!help")))
def say_comment_help(message, say):
    print_comein = ''' < 명령어 도움말 >
    !출근 : 현재시간으로 출근 처리가 됩니다.
    !퇴근 : 현재시간으로 퇴근 처리가 됩니다.
    !자리비움 (시간) : 현재시간부터 해당 시간만큼 자리비움(오프) 상태로 처리됩니다.
    '''
    
    say(text=print_comein, channel = message['channel'])


# main 실행문
if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()