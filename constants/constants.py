# token
from constants.get_token import getSlackToken

# Constants
TOKEN_LINK = 'assets/slack_token.json'
READ_MODE = 'r'

ASIA_SEOUL = 'Asia/Seoul'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

SLACK_APP_TOKEN, SLACK_BOT_TOKEN = getSlackToken(TOKEN_LINK, READ_MODE)
HELP, GTW, LTW, OW = "!도움"
HELP_HEADLINE = "\n< 명령어 도움말 >\n"
