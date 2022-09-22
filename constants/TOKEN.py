# TOKEN 관련 상수
from util.token import getSlackToken

# Constants
TOKEN_LINK = 'assets/slack_token.json'
READ_MODE = 'r'

# token
SLACK_APP_TOKEN, SLACK_BOT_TOKEN = getSlackToken(TOKEN_LINK, READ_MODE)
