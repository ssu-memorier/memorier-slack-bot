import json


def getUserId(userPath, mode):      # 유저 데이터를 가져오는 함수
    with open(userPath, mode, encoding='utf-8') as f:
        keys = json.load(f)

    return keys["user_id"]
