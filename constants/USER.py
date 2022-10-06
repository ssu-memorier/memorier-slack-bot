from utils.getId import getUserId
from constants import TOKEN

USER_LINK = 'assets/user_info.json'

# User name in team
NAME = getUserId(USER_LINK, TOKEN.READ_MODE)
