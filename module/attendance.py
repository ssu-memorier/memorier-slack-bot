from module.utils import *

workingTime = [10,10,0]            # 출근 시간(지각 처리 기준시간)

# !출근
def GoToWork(message, say):
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    
    # 10시 10분 넘어서 출근을 하면 지각 처리
    if date.time().hour >= workingTime[0] and date.time().minute >= workingTime[1]:
        state = "late"
    else:
        state = "gtw"
    
    workOutput = printWorkState(message, date, state)
    
    printCommandLogs(message, "!출근")      # 로그 출력
    say(text=workOutput, channel = '출석-체크')

# !퇴근
def LeaveToWork(message, say):
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, "ltw")
    
    printCommandLogs(message, "!퇴근")      # 로그 출력
    say(text=workOutput, channel = '출석-체크')

# !오프 (시간)
def OfflineWork(message, say):
    date = getCurrentSeoulTime()       # 현재시간을 가져온다
    workOutput = printWorkState(message, date, "ow")
    
    printCommandLogs(message, "!오프")      # 로그 출력
    say(text=workOutput, channel = '출석-체크')

# 출력할 메세지 생성기
def printWorkState(message, date, state):
    workState = {"gtw" : "출근", "ltw" : "퇴근", "ow" : "자리비움", "late" : "지각"}
    
    if state == "ow":
        duringTime = message['text'].split()[1]     # 자리비움 시간
        return f"[ <@{message['user']}> ] {date.strftime('%Y-%m-%d %H:%M:%S')}\t{duringTime}시간 {workState[state]}"
    else:
        return f"[ <@{message['user']}> ] {date.strftime('%Y-%m-%d %H:%M:%S')}\t{workState[state]}"