# 입력 처리
x = int(input())

# dp 테이블
d = [0] * 30001 # 정수 X는 최대 30000 까지임.

# dp 채우기
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    # 2,3,5 로 나눠 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])