# 한 붓 그리기
# 모든 정점 방문이 아닌, 모든 간선을 거쳐야 함 (모든 항공권 사용)
# 택할 수 있는 간선이 2개 이상인 경우, 알파벳 순서에 우선함

# ICN에서 시작, 알파벳 우선으로 갈 수 있는 곳을 선택
# 만약 갈 수 있는 곳이 없다면 스택에서 제거 후 다른 선택지를 선택

# 스택과 재귀를 이용한 한 붓 그리기 문제
# 깊이 우선 탐색을 응용하여 한 붓 그리기

# 딕셔너리를 활용하여 각 공항에서 출발하는 항공권의 리스트를 표현해보자
# ex) ICN -> [ATL, SFO], ATL -> [ICN, SFO], SFO -> [ATL]
# 파이썬에서 리스트는 뒤에서 제거하는 것이 효율적이므로, 알파벳 역순으로 정렬하자.

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    # 알파벳 역순으로 정렬
    for r in routes:
        routes[r].sort(reverse=True)
    print(routes)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        print(stack, path)
        top = stack[-1] # 스택의 제일 위에 있는 원소
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1]) # 알파벳 역순이므로 마지막 원소로 가야함
            routes[top] = routes[top][:-1]
        
    return path[::-1] # 역순으로