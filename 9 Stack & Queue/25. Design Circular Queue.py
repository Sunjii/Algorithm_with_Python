# https://leetcode.com/problems/design-circular-queue/
# 원형 큐 구현

# 큐와 유사한 구조. 단, 첫 요소가 마지막 요소와 연결된다는 것이 차이점.

class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.head = 0
        self.tail = 0
    
    def enQueue(self, value):
        if self.q[self.tail] is None:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.maxlen
            return True
        else:
            return False
    
    def deQueue(self):
        if self.q[self.head] is None:
            return False
        else:
            self.q[self.head] = None
            self.head = (self.head + 1) % self.maxlen
            return True
        
    def Front(self):
        return -1 if self.q[self.head] is None else self.q[self.head]
    
    def Rear(self):
        return -1 if self.q[self.tail -1] is None else self.q[self.tail - 1]
    
    def isEmpty(self):
        return self.head == self.tail and self.q[self.head] is None
    
    def isFull(self):
        return self.head == self.tail and self.q[self.head] is not None


cq = MyCircularQueue(5)
cq.enQueue(10)
cq.enQueue(20)
cq.enQueue(30)
cq.enQueue(40)
print(cq.Rear())
print(cq.isFull())
cq.deQueue()
cq.deQueue()
cq.enQueue(50)
cq.enQueue(60)
print(cq.Rear())
print(cq.Front())