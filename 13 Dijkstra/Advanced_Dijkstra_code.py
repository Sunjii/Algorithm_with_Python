# 우선순위 큐를 활용하면 최단거리가 가장 짧은 노드를 고르는 과정을 단축할 수 있다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 짧은 최단거리 노드
        dist, now = heapq.heappop(q)
        # 방문한 곳이면 무시
        if distance[now] < dist:
            continue
        # 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])