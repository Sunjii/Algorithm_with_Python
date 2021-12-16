# 특정 지점으로 가는 최단 거리를 구하는 문제이다. BFS가 적절하다
# BFS를 수행하여 모든 노드로 가는 거리를 넣으면 된다.
# 탐색 방향은 상하좌우이고, 괴물이 없다면 (1 이라면) 탐색 가능하다

# BFS를 위한 deque import
from collections import deque

# 입력 처리
n, m = map(int,input().split())
# 맵 정보 처리. 괴물이 있으면 0, 없으면 1.
# 이후 탐색시 거리 +1 마다 +1 처리
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동방향 정의 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖인 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # new 노드를 처음 방문하는 경우 최단거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))