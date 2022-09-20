from module.utils import printCommandLogs

commandList = {
    "!출근" : "현재시간으로 출근 처리가 진행됩니다.",
    "!퇴근" : "현재시간으로 퇴근 처리가 진행됩니다.",
    "!자리비움 (시간)" : "현재시간부터 해당 시간만큼 자리비움(오프) 상태로 처리됩니다.",
    "!도움" : "실행가능한 전체 명령어에 대해 나오게 됩니다."
}

# !도움
def helpCommend(message, say):
    helpOutput = "\n< 명령어 도움말 >\n"
    
    for command, info in commandList.items():
        helpOutput += f"{command} : {info}\n"
    
    printCommandLogs(message, "!도움")      # 서버에 log를 따로 남김
    say(text=helpOutput, channel = message['channel'])