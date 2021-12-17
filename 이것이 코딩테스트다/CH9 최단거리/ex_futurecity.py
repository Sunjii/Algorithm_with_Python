# A가 K를 방문하고 X를 방문하려고 한다.
# 이 때 가능한 최단거리는?

# 1번 노드에서 X를 거쳐 K로 가는 최단 거리는
# 1~X + X~K 이다

INF = int(1e9)
# 입력 처ㅣㄹ
n,m = map(int, input().split())
# 그래프 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 간선 정보 입력 처리
for _ in range(m):
    # 모든 비용은 1로 동일하다
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐가는 k와 최종 목적지 x 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
# 결과 출력
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)