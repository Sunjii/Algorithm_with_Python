# https://leetcode.com/problems/maximum-depth-of-binary-tree
# 이진 트리의 최대 깊이를 구하라

# 이진 트리의 깊이는 BFS 로 구할 수 있다.
# 여기서, DFS는 스택, BFS는 큐를 사용하여 구현한다.

import collections

def maxDepth(root):
    ...
    queue = collections.deque([root])
    depth = 0

    while queue:
        ...
    return depth