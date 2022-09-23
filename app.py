# -*- coding: utf-8 -*-

# User Defined Functions
from command.commands import addAttendanceCommand
from constants import TOKEN      # Slack App/Bot Token

# Python Libraries
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# App Loading
app = App(token=TOKEN.SLACK_BOT_TOKEN)
addAttendanceCommand(app)


def main():  # Main Process
    print("="*10, "SlackBot is started", "="*10, '\n'*2)       # slackbot 시작
    SocketModeHandler(app, TOKEN.SLACK_APP_TOKEN).start()


if __name__ == "__main__":
    main()
