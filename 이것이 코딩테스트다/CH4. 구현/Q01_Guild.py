# 공포도를 정렬
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 현재 그룹의 모험가 수와 추가할 모험가의 공포도 비교
count = 0
result = 0

for i in data:
    count += 1  # 모험가 추가
    if count >= i:
        # 현재 그룹의 모험가의 숫자가 공포도 보다 높으면 추가 가능
        result += 1
        count = 0

print(result)
