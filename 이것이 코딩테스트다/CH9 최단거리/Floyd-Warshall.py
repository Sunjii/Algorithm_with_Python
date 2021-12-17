INF = int(1e9)

# 노드와 간선의 개수 입력
n = int(input())
m = int(input())

# 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신과의 거리는 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 간선 정보 입력 및 처리
for _ in range(m):
    # a -> b 의 비용은 c
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()