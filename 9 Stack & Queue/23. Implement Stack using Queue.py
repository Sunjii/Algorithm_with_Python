# https://leetcode.com/problems/implement-stack-using-queue/
# 큐를 이용해 push, pop, top, empty 연산을 지원하는 스택을 구현하라


import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque() # deque로 구현한다.
    
    def push(self, num):
        self.q.append(num)
        # 삽입 후 맨 앞으로 오도록 정렬
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())
        
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0


stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
print(stack.top())