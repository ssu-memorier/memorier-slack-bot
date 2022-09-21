import json

def getSlackToken(TOKEN_LINK, READ_MODE):
    # go to Keys and get dictionary
    with open(TOKEN_LINK, READ_MODE) as f:
        keys = json.load(f)
        
    # get Token
    slack_bot_token = keys['slack_token']['slack_bot_token']
    slack_app_token = keys['slack_token']['slack_app_token']
    
    return slack_app_token, slack_bot_token
