# https://leetcode.com/problems/palindrome-linked-list/
# 연결 리스트가 팰린드롬 구조인지 판별하라

# input : 1->2 output : false
# input : 1->2->2->1 output : true

# sol 1) 리스트로 변환
# 팬릴드롬 판별을 위해서는 리스트의 앞과 끝을 비교해가면 된다.
# 연결리스트를 파이썬의 리스트로 변환하여 리스트의 기능을 활용하자.
import collections
from typing import Collection, Deque, List

def isPalindrome(head):
    q: List = []

    if not head:
        return True

    node = head
    # 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팬릴드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
        return True

# sol 2) deque를 이용한 최적화
# q.pop(0)처럼 리스트의 '첫번째' 요소 추출은 비효율적인 작업이다. 리스트의 모든 요소들이 한 칸씩 시프팅되기 때문이다.
# 이러한 시프팅 과정은 O(n)의 복잡도를 가지기도 한다.
# 파이썬의 deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 O(1)의 복잡도가 걸린다. 따라서 데큐를 사용하여 최적화를 하자

def isPalindrome_deque(head):
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True

# sol 3) runner를 이용한 풀이