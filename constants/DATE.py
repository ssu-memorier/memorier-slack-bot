# 현재 시간을 구할때 사용하는 상수
HOUR = 'hour'       # 시(HH)
MIN = 'minutes'     # 분(MM)
START_TIME, END_TIME = 'startTime', 'endTime'       # 시작시간, 종료시간을 나타내는 상수
HH = 0      # 시(HH) index
MM = 1      # 분(MM) index
SS = 2      # 초(SS) index

ASIA_SEOUL = 'Asia/Seoul'       # 서울 지역을 나타냄
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'       # 출력 내용 (년-월-일 시:분:초)

LATE_TIME = {'HOUR': 10, 'minutes': 10}     # 지각 처리 시간
CORETIME = {         # 코어타임 (20:00:00~23:00:00)
    START_TIME: [20, 0, 0],     # [HH,MM,SS]
    END_TIME: [23, 0, 0]     # [HH,MM,SS]
}
