def solution(triangle):
    answer = 0
    
    
    # 현재 위치를 k행 n번째라고 했을 때
    # 갈 수 있는 위치는 k+1행의 n과 n+1
    # list[k][n] + (list[k+1][n] OR list[k+1][n+1])
    # 의 값이 최대가 되도록 해야한다.
    '''
    if n == 0:
        dp[k][n] = dp[k-1][n] + triangle[k][n]
    elif n == k:
        dp[k][n] = dp[k-1][n-1] + triangle[k][n]
    else:
        dp[k][n] = triangle[k][n] + max(dp[k-1][n], dp[k-1][n-1])
    
    '''
    
    dp = [[0 for i in range(len(triangle))] for j in range(len(triangle))] 
    
    for k in range(len(triangle)):
        for n in range(len(triangle[k])):
            if n == 0:
                dp[k][n] = dp[k-1][n] + triangle[k][n]
            elif n == k:
                dp[k][n] = dp[k-1][n-1] + triangle[k][n]
            else:
                dp[k][n] = triangle[k][n] + max(dp[k-1][n], dp[k-1][n-1])
            answer = max(answer, dp[k][n])
    
    return answer