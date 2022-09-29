from utils.getItem import getUserId
from constants import TOKEN

USER_LINK = 'assets/user_info.json'

# User name in team
USER_NAME = getUserId(USER_LINK, TOKEN.READ_MODE)
