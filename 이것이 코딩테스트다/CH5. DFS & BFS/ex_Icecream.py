# 0은 벽이 없는 부분 1은 벽이 있는 부분이다.
# 따라서 0으로 연결된 부분은 전체가 하나가 된다.
# 따라서 문제는 곧 0으로 연결된 부분을 찾는 '탐색' 문제


'''
DFS
1. 상하좌우 살펴보고 값이 0이면서 방문하지 않으면 방문
2. 더이상 방문할 곳이 없을때 까지 반복
3. 모든 노드에 반복하여 방문하지 않은 지점의 수를 센다

'''

# 입력 처리
n, m = map(int, input().split())

# 맵 정보 처리
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
# DFS
def dfs(x,y):
    # 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드가 방문하지 않은 노드라면
    if graph[x][y] == 0:
        # 해당 노드를 방문처리함
        graph[x][y] = 1
        # 상하좌우 재귀처리
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    # graph[][] == 1 이라는 것은 이미 방문한 곳이다. 따라서 더 아이스크림을 만들 수 없다.
    return False


# 모든 노드애 데해 음료수를 채우자
result = 0
for i in range(n):
    for j in range(m):
        # 각 위치에서 DFS를 수행
        if dfs(i,j) == True:
            result += 1

print(result)