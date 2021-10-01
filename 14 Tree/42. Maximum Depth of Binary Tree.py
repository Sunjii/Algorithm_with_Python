# https://leetcode.com/problems/maximum-depth-of-binary-tree
# 이진 트리의 최대 깊이를 구하라

# 이진 트리의 깊이는 BFS 로 구할 수 있다.
# 여기서, DFS는 스택, BFS는 큐를 사용하여 구현한다.

import collections

def maxDepth(root:TreeNode):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        # 깊이 추가
        depth += 1
        # 큐 연산 추출 노드를 자식 노드로 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            # 자식 노드 유무 판별
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        
        # BFS의 반복 횟수가 곧 깊이가 된다.
    return depth

root = [3,9,20, None, None, 15, 7 ]
print(maxDepth(root))