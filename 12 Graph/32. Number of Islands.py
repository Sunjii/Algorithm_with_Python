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


def solutions(grid:List[List[str]]):
    # 예외 처리
    if not grid:
        return 0
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    
    return count


def dfs(grid:List[List[str]], i, j):
    # g[i][j] 에서 4방향 탐색을 진행한다. '0'이 나올때 까지
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
            return
    
    print(grid, grid[i][j])
    print(type(grid[i][j]))
    grid[i][j].replace('1', '0') # 방문한 곳은 1을 지워서 중복계산을 방지한다.
    #grid[i][j].replace('1', '0')
    print(grid[i][j])

    # 4방향 탐색 (재귀)
    '''
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    '''


input = ['11110',
'11010',
'11000',
'00000']

print(solutions(input))