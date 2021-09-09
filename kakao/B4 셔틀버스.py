'''
셔틀 운행 횟수 n (0 < n <= 10)
셔틀 운행 간격 t (0 < t <= 60)
셔틀 탑승 가능 m (0 < m <= 45)
각 크루의 탑승장 도착시간 timetable. 길이는 2000까지 가능하며, HH:MM 형식으로 이루어짐

셔틀은 09:00부터 운행을 시작하며, t분 간격으로 n회 운행함.

출력 : 제일 늦은 도착시간

'''


def solution(n, t, m, timetable):
    # 먼저 timetable을 변형하는 작업이 필요하다. HH:MM 이니까, 분로 계산하면 편할듯.
    for i, time in enumerate(timetable):
        timetable[i] = int(time[:2]) * 60 + int(time[3:])
    timetable.sort()
    print(timetable)

    current = 540 # 09:00
    for a in range(n):
        for b in range(m):
            if timetable and timetable[0] <= current:
                # 출발 전 도착한 사람들
                targetTime = timetable.pop(0) -1 # 1분 먼저 와야 함
            else:
                targetTime = current
        # 다음 셔틀 도착시간
        current += t

    hour, minit = divmod(targetTime, 60)
    hour = str(hour).zfill(2)
    minit = str(minit).zfill(2)

    return f"{hour}:{minit}"



timetable = ["23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]
timetable2 = ["09:00","09:00","09:00","09:00"]


print(solution(10,60,45, timetable))
print(solution(2,1,2, timetable2))
