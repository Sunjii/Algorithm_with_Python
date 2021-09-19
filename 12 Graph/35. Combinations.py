# https://leetcode.com/problems/combinations/
# 전체 수 n을 입력받아 k개의 조합을 리턴하라

'''
input
n = 4, k = 2
output
[ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4] ]
'''

# 조합의 경우의 수는 n! / k!(n-k)! 이다.
# 1~n 까지의 수에서 k개를 선택

def solution(n, k):
    result = []

    # 조합의 경우 자기 자신과 앞의 모든 선택된 요소를 배제하고 뽑아야한다.
    def dfs(elements, start, k):
        if k == 0:
            # 결과에 삽입한다.
            result.append(elements[:]) # 참조 처리 방지를 위한 [:] 으로 copy
            
            # 이전의 모든 값을 고정하고 재귀처리
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    
    dfs([], 1, k)
    return result

# sol2) itertools 모듈 사용
import itertools
def combine(n, k):
    return list(itertools.combinations(range(1, n+1), k))

n = 5
k = 3
print(solution(n, k))
print(combine(5,3))
