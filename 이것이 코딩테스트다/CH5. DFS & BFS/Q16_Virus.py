n, m = map(int,input().split())
data = []

# 벽 설치한 뒤의 맵
temp =[[0] * m for _ in range(n)]

# 이동방향 정의 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


# DFS로 바이러스 퍼뜨리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    # 해당 좌표의 인접한 곳이면 바이러스 번파
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if temp[nx][ny] == 0:
            # 바이러스 배치 및 재귀
            temp[nx][ny] = 2
            virus(nx, ny)
    
# 안전 영역 계산
def safe():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

# DFS 로 울타리 설치하면서 안전영역 계산하기
def DFS(count):
    global result
    # 울타리 3개 설치가 되었으면 종료
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스 전파 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, safe())
        return
    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                DFS(count)
                data[i][j] = 0
                count -= 1
                
DFS(0)
print(result)
        