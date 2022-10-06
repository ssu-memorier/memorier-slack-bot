# 현재 시간을 구할때 사용하는 상수
HOUR = 'hour'       # 시(HH)
MIN = 'minutes'     # 분(MM)

START_TIME = "startTime"    # 시작시간
END_TIME = "endTime"        # 종료시간

ASIA_SEOUL = 'Asia/Seoul'       # 서울 지역을 나타냄
BASE_TIME = 'Etc/GMT+1'     # 서울 : 10시 == GMT+1 : 00시 (출석체크 및 주간보고서에 사용할 시간)
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'       # 출력 내용 (년-월-일 시:분:초)

DIFF_TIMESTAMP_GMT9 = 3600*9        # GMT+9 와의 timestamp 차이
WORKINGHOUR = 8         # 근무시간

ATTENDANCE_TIME = {
    START_TIME: {
        HOUR: 9, MIN: 30
    }, END_TIME: {
        HOUR: 10, MIN: 10
    }
}     # 지각 처리 시간

CORE_TIME = {
    START_TIME: {
        HOUR: 20, MIN: 0
    }, END_TIME: {
        HOUR: 23, MIN: 0
    }
}       # 코어 타임

SLEEPING_TIME = {
    START_TIME: {
        HOUR: 0, MIN: 0
    }, END_TIME: {
        HOUR: 9, MIN: 00
    }
}     # 출근 할 수 없는 취침시간
