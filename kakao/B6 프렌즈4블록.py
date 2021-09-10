'''
2x2 사이즈 블록이 지워진다
1. 일치여부 찾기
2. 일치한 위치를 삭제
3. 빈 공간을 채우기 (낙하)
'''


def solution(m, n, board):
    # 높이 m, 폭 n

    board = [list(x) for x in board]
    matched = True

    # 1. 일치여부 찾기
    # b[n][k] b[n][k+1] b[n+1][k] b[n+1][k+1] 
    while matched:
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == \
                    board[i][j+1] == \
                    board[i+1][j] == \
                    board[i+1][j+1] != '#':
                    matched.append([i,j])

        # 2. 일치한 위치를 삭제
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#'

        # 3. 빈공간 처리
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '#':
                        board[i+1][j], board[i][j] = board[i][j], '#'
        
    answer = sum(x.count('#') for x in board)
    return answer

input1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(4,5, input1))