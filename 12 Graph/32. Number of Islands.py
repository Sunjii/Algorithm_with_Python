# https://leetcode.com/problems/number-of-islands/
# 섬의 갯수를 구하라

'''
input
11110
11010
11000
00000
output : 1
'''

# 각 점을 동서남북으로 연결된 그래프라고 할 수 있다.
# 네 방향으로 DFS를 이용하여 1을 찾아본다.
# 0 이 나온다면 육지의 끝이 된다.
# 더 이상 1을 못 찾는 경우라면 섬의 카운트를 1 늘린다.

from typing import List

class Solution:
    def numIslands(grid:List[List[str]]):
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                    return

            grid[i][j] = 0
            # 재귀
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count

    input = ['11110',
    '11010',
    '11000',
    '00000']

    print(numIslands(input))
