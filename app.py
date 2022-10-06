# -*- coding: utf-8 -*-

# User Defined Functions
from utils.manageCommands import addAllCommands
from constants import TOKEN      # Slack App/Bot Token

# Python Libraries
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# App Loading
app = App(token=TOKEN.SLACK_BOT_TOKEN)
addAllCommands(app)       # 봇에서 실행하는 모든 커맨드 불러오기


def main():  # Main Process
    print("="*10, "SlackBot is started", "="*10, '\n')       # slackbot 시작 출력문
    SocketModeHandler(app, TOKEN.SLACK_APP_TOKEN).start()


if __name__ == "__main__":
    main()
