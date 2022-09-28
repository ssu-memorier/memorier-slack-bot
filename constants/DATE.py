# 현재 시간을 구할때 사용하는 상수
HOUR = 'hour'       # 시(HH)
MIN = 'minutes'     # 분(MM)

ASIA_SEOUL = 'Asia/Seoul'       # 서울 지역을 나타냄
BASE_TIME = 'Etc/GMT+1'     # 서울 : 10시 == GMT+1 : 00시 (출석체크 및 주간보고서에 사용할 시간)
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'       # 출력 내용 (년-월-일 시:분:초)

LATE_TIME = {
    HOUR: 10,
    MIN: 10
}     # 지각 처리 시간
