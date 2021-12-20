# n개의 도시 m개의 간선
# 거리는 모두 1
# 특정 도시 X로부터 출발하여 최단거리가 K인 모든 도시의 번호를 출력하라

from collections import deque

# 입력 처리
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 간선 정보 입력 처리
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# BFS 수행
q = deque([x])
while q:
    print(q)
    now = q.popleft()
    # 이동 가능한 정점 확인
    for next_node in graph[now]:
        # 방문하지 않았다면 방문하자
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리 K인 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print("해당 하는 도시는 없습니다.")
