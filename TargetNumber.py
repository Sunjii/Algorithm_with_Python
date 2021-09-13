'''
def solution(numbers, target):
    numbers.sort()   
    # 더하거나 빼거나의 이진트리
    # 모든 방법의 숫자를 구해야 한다 --> DFS
    global answer
    answer = 0
    def DFS(depth, value):
        # step 1. 종료조건
        global answer
        if (depth == len(numbers) and value == target):
            answer += 1
            return
        elif (depth == len(numbers)):
            # 없는 경우
            return
        else:
            # 더 내려가야 함
            depth += 1     
        DFS(depth, value+numbers[depth-1])
        DFS(depth, value-numbers[depth-1])           
    DFS(0, 0)    
    return answer
'''

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    print(s)
    return s.count(target)