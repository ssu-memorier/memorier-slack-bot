import json


def getUserId(userPath, mode):      # 유저 데이터를 가져오는 함수
    with open(userPath, mode, encoding='utf-8') as f:
        keys = json.load(f)

    return keys["user_id"]


def getBotChannelId(tokenPath, mode):     # 봇 채널ID를 가져오는 함수
    # go to Keys and get dictionary
    with open(tokenPath, mode, encoding='utf-8') as f:
        keys = json.load(f)

    # get Token
    slack_bot_channelID = keys['slack_token']['slack_bot_channelID']

    # get test Token : test 진행할 때 사용하는 TOKEN (평상시 사용 X)
    # slack_bot_channelID = keys['slack_test_token']['slack_bot_channelID']

    return slack_bot_channelID
