# https://leetcode.com/problems/subsets/
# 모든 부분 집합을 리턴

'''
input : nums = [1,2,3]
output : [ [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3], [] ]
'''

# 중복이 허용되지 않는다.
# 모든 탐색의 경로가 정답이 된다. 따라서 탐색할 때마다 결과를 추가하면 된다.

def solution(nums):
    result = []

    def dfs(index, path):
        # 매번 결과에 추가
        result.append(path)

        # 경로를 만들면서 계속 DFS
        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]])
    
    dfs(0, [])
    return result

nums = [1,2,3,4,5]
print(solution(nums))