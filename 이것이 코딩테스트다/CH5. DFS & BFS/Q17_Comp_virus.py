from collections import deque

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        # 바이러스가 존재하는 경우 바이러스 정보 삽입
        if graph[i][j] != 0:
            # virus, 시간, x y 좌표
            data.append((graph[i][j], 0, i, j))
        
# 정렬 후 큐에 복사. (낮은 번호가 우선적으로 전염)
data.sort()
q = deque(data)

# 입력 처리
target_s, target_x, target_y = map(int, input().split())

# 이동방향 정의 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 진행
while q:
    # 바이러스 번호가 낮은 순의 우선순위 큐가 된다
    virus, s, x, y = q.popleft()
    # s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 4방향 확인 후 전염
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동 가능하면 전염
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))


print(graph[target_x-1][target_y-1])