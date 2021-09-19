# https://leetcode.com/problems/combination-sum
# 숫자 집합 candidate를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복 가능하다.

'''
input
candidate = [2,3,6,7], target = 7
output
[ [7], [2,2,3] ]
'''

# sol 1) DFS를 통한 중복 조합 그래프 탐색

def solution(candidates, target):
    result = []

    def dfs(csum, index, path):
        # 종료 조건 - 가지치기
        if csum < 0:
            return
        if csum == 0: # 0인 경우 정답
            result.append(path)
            return
        
        # 자신부터 하위 원소까지 나열
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
        
    dfs(target, 0, [])
    return result

c1 = [2,3,6,7]
t1 = 7
c2 = [2,3,5]
t2 = 8
print(solution(c1, t1))
print(solution(c2,t2))