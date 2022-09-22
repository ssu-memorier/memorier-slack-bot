# -*- coding: utf-8 -*-

# User Defined Functions
from command.commands import getAttendanceCommand
from constants import TOKEN      # Slack App/Bot Token

# Python Libraries
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# App Loading
app = App(token=TOKEN.SLACK_BOT_TOKEN)
getAttendanceCommand(app)


def main():  # Main Process
    SocketModeHandler(app, TOKEN.SLACK_APP_TOKEN).start()


if __name__ == "__main__":
    main()
