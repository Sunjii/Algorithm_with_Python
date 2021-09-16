# https://leetcode.com/problems/implement-queue-using-stack/
# 스택을 이용해 push, pop, peek, empty 연산이 있는 큐를 구현하라.

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, num):
        self.input.append(num)
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        # output이 없다면 input에 있는 모든 값을 입력시킨다.
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.empty())