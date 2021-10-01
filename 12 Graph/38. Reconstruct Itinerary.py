# https://leetcode.com/problems/reconstruct-itinerary/
# [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전순으로 방문한다.

'''
input : [ ["MLC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"] ]
output : ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''

# 1) Graph를 구성
'''
graph = {
    "From1" : ["To1", "To2", ..],
    "From2" : ["To1", "To3", "To5", ..], ..
}

graph = collections.defaultdict(list)
for a, b in tickets:
    graph[a].append(b)
for a in graph:
    graph[a].sort()

'''
# 2) Graph에서 하나씩 꺼내면서 DFS

import collections
def solution(tickets):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
        print(graph[a])
    
    route = []
    def dfs(a):
        # 어휘순으로 방문한다
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs("JKF")
    # 다시 뒤집어서 어휘순으로 정렬하고 리턴
    return route[::-1]


input = [ ["MLC", "LHR"], ["JFK", "MLC"], ["SFO", "SJC"], ["LHR", "SFO"] ]
print(solution(input))