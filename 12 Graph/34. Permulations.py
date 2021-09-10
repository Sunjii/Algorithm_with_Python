# https://leetcode.com/problems/permulations/
# 주어진 정수로 만들 수 있는 모든 순열을 출력

'''
input : [1,2,3]
output: [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2].
    [3,2,1]
]
'''

# 순열의 가지 수는 n! 이다.
# 그래프를 이용해볼 수 있다.
'''
_
1           2       3
12 13       21  23  31   32
123 132     213 231 ...
'''
def solution(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        # leaf node
        if len(elements) == 0:
            result.append(prev_elements[:]) 
            # [:] 를 하는 이유  는 deepcopy를 하기 위함이다.
            # 만약 [:]를 하지 않는 경우, 참조가 추가되게 되므로 값이 변경될때 같이 바뀌어 버린다.

        # 순열 생성
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop(0)
    
    dfs(nums)
    return result

import itertools
def permute(nums):
    return list(map(list, itertools.permutations(nums)))


input = [1,2,3,4]
print(solution(input))
print(permute(input))