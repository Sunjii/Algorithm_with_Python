# 합이 작다면 절단기의 높이를 낮추고 합이 더 크다면 절단기의 높이를 높인다
# 이 때 이진탐색을 이용하여 절단기의 적절한 높이를 찾아가면 된다.


# 입력처리
n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))

# 시작과 끝 점 설정
s = 0
e = max(arr)

# 이진탐색 수행
result = 0
while(s < e):
    total = 0
    # mid는 절단기의 높이
    mid = (s+e) // 2
    
    for x in arr:
        if x > mid:
            total += x - mid
    
    # 더 잘라야 하는 경우
    if total < m:
        end = mid - 1
    else:
        # 초과한 경우
        result = mid # 우선 기록
        s = mid + 1

print(result)