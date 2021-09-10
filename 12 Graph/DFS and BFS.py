'''

'''
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

# 정점 v에서 시작하여 탐색
def recursive_dfs(v, discorverd=[]):
    discorverd.append(v)
    for w in graph[v]:
        if not w in discorverd:
            discorverd = recursive_dfs(w, discorverd)
    
    return discorverd

print(recursive_dfs(1))

'''
큐를 이용한 BFS. 일반적으로 최단경로를 찾을때 쓰인다.
모든 인접 간선을 추출하고 도착점인 정점을 큐에 삽입한다.
'''
def iterative_bfs(start_v):
    discorverd = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discorverd:
                discorverd.append(w)
                queue.append(w)
    return discorverd

print(iterative_bfs(1))

