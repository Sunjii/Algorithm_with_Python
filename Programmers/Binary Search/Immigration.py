import math
def solution(n, times):
    answer = 0
    times.sort()
    
    # 심사시간이 최대로 되는 case는 n x max(times)이다.
    # 이때 걸리는 시간을 maxtime이라고 하자.
    # 각 심사관 i는 그 시간동안 maxtime / times[i] 명을 처리할 수 있다.
    
    # midtime = maxtime / 2 라고 하고,
    # 전체 심사위원의 mid / times[i] 합들이 n과 같아지는 경우가 곧 mid==최소시간(answer)이 될 것이다.
    
    maxtime = n * max(times)
    while answer != maxtime:
        mid = math.trunc((answer + maxtime) / 2)
        sums = 0
        # midtime 동안 각 통과자들의 sum을 구한다.
        for i, _ in enumerate(times):
            sums += math.trunc(mid / times[i])
        if(sums >= n):
            # 통과자가 더 많다면 시간을 더 줄여본다.
            maxtime = mid
        else:
            # 통과자가 모자른 경우 최소시간을 늘려 다시 탐색
            answer = mid + 1
    
    return answer