# TOKEN 관련 상수
from utils.token import getSlackToken, getUserId

# Constants to get TOKEN
TOKEN_LINK = 'assets/slack_token.json'
USER_LINK = 'assets/user_info.json'
READ_MODE = 'r'

# token
SLACK_APP_TOKEN, SLACK_BOT_TOKEN = getSlackToken(TOKEN_LINK, READ_MODE)

# User name in team
USER_NAME = getUserId(USER_LINK, READ_MODE)
