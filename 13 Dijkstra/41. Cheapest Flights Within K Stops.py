# https://leetcode.com/problems/cheapest-flights-within-k-stops
# 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴.
# 경로가 존재하지 않는 경우 -1 리턴

# Sol) Dijkstra
import collections
import heapq

def solution(flights, src, dst, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u,v,w in flights:
        graph[u].append((v,w))
    
    # 큐 변수 : [ (소요시간, 정점, 남은 경유횟수) ]    
    Q = [(0, src, K)]

    # 우선순위 큐 최소값을 기준으로 정점까지 최단 경로 삽입
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                # alt 계산 후 큐를 갱신
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))

    return -1

n = 3
edges = [[0,1,100], [1,2,100], [0,2,500]]
src = 0
dst = 2
K = 0

print(solution(edges, src, dst, K))