'''
다익스트라 알고리즘

처음에는 각 노드에 대한 최단거리를 담는 1차원 리스트를 선언한다. 그 다음 방문할 수 있는 곳 까지의 최단거리를 구한다.
이후 단계마다 방문하지 않은 노드들 중에서 최단거리가 가장 짤은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인.
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선 입력 처리
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담고있는 리스트 생성
graph = [[] for i in range(n+1)]
# 방문 확인용 리스트
visited = [False] * (n+1)
# 최단거리 테이블 초기화
distance = [INF] * (n+1)

# 간선 정보 처리
for _ in range(m):
    # 노드 A --> B의 비용이 C
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
# 방문하지 않은 노드에서 가장 최단거리의 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        # 최단거리 노드를 꺼내 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

