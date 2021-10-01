# https://leetcode.com/problems/network-delay-time

# 노드 K에서 출발하여 모든 노드가 신호를 받을 수 있는 시간을 계산. 불가능한 겨우 -1을 리턴.
# 입력값 (u, v, w)는 각각 출발지, 도착지, 소요시간이며, 전체 노드의 개수는 N이다.


# Sol 1) Dijstrak 
# 모든 노드가 신호를 받는데 걸리는 시간과, 도달 여부를 구해야한다.
# 가장 오래 걸리는 노드가 곧 시간이 된다.
# 만약 어느 한 곳이라도 도달하지 못 하는 경우에는 -1을 리턴한다.
 
import collections
import heapq

def solution(times, N, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u,v,w in times:
        graph[u].append((v,w))
    
    # 큐 변수 : [ (소요시간, 정점) ]    
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최소값을 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                # alt 계산 후 큐를 갱신
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단경로 존재 여부 판별
    if len(dist) == N:
        # 모든 노드가 연결되어있음
        return max(dist.values())
    return -1

times = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
N = 8
K = 3
print(solution(times,N,K))