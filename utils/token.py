import json


def getSlackToken(tokenPath, mode):     # slack Token을 가져오는 함수
    # go to Keys and get dictionary
    with open(tokenPath, mode, encoding='utf-8') as f:
        keys = json.load(f)

    # get Token
    slack_bot_token = keys['slack_token']['slack_bot_token']
    slack_app_token = keys['slack_token']['slack_app_token']

    # get test Token : test 진행할 때 사용하는 TOKEN (평상시 사용 X)
    # slack_bot_token = keys['slack_test_token']['slack_bot_token']
    # slack_app_token = keys['slack_test_token']['slack_app_token']

    return slack_app_token, slack_bot_token
