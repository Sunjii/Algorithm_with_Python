# 주어진 수열에서 한 칸씩 띄워서 골라서 가장 큰 합을 찾는 문제

'''
점화식

i-1번을 고르면 i번은 고를 수 없다.
i-2번을 고르면 i번은 고를 수 있다.

따라서 위 2가지 경우 중 더 많은 합이 나오는 경우를 택하면 된다.
'''

#입 력 처리
n = int(input())
arr = list(map(int, input().split()))

# dp 테이블 초기화
dp = [0]*100

# dp 진행. sum을 넣는다.
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
print(dp[n-1])