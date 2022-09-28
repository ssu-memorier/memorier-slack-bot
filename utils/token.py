import json


def getSlackToken(tokenPath, mode):
    # go to Keys and get dictionary
    with open(tokenPath, mode) as f:
        keys = json.load(f)

    # # get Token
    # slack_bot_token = keys['slack_token']['slack_bot_token']
    # slack_app_token = keys['slack_token']['slack_app_token']

    # get test Token
    slack_bot_token = keys['slack_test_token']['slack_bot_token']
    slack_app_token = keys['slack_test_token']['slack_app_token']

    return slack_app_token, slack_bot_token


def getUserId(userPath, mode):
    with open(userPath, mode) as f:
        keys = json.load(f)

    return keys["user_id"]
