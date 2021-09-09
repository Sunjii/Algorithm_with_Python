'''
파이썬의 deque는 최대 길이를 지정할 수 있다. 이 경우 새로 추가되는 아이템은 가장 오래된 아이템을 대체하게 된다.


'''
import collections

def solution(cacheSize, cities):
    time = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()
        # hit
        if c in cache:
            cache.remove(c)
            cache.append(c)
            time += 1
        # miss
        else:
            cache.append(c)
            time += 5
    return time

input1 = ['Jeju', 'Pangyo', 'Seoul', 'New York', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'New York', 'LA']
input2 = ['Jeju', 'Pangyo', 'Seoul', 'New York', 'LA']
input3 = ['jeju', 'pangyo', 'NewYork', 'newyork']
print(solution(3, input1))
print(solution(0, input2))
print(solution(2, input3))