import math


def solution(progresses, speeds):
    answer = []
    left_days = []

    # 각 작업별 남은 일수 계산
    # (100 - p[a]) / s[a] .올림
    for i in range(len(progresses)):
        left_days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    def minusDay():
        # 일수를 하나씩 뺀다. 맨 앞 원소가 0이 될때 까지
        while left_days[0] > 0:
            temp = left_days[0]
            for i in range(len(left_days)):
                left_days[i] -= temp

    def bapho():
        # 맨 앞에서 부터 배포하되, 뒤의 0 이하인 케이스들과 함께 배포 (pop)
        while left_days and left_days[0] <= 0:
            count = 0
            while left_days and left_days[0] <= 0:
                if left_days[0] <= 0:
                    left_days.pop(0)
                    count += 1
            answer.append(count)

    while left_days:
        minusDay()
        bapho()

    return answer
