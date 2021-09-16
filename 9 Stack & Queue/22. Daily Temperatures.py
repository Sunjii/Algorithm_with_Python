# https://leetcode.com/problems/daily-temperatures/
# 매일 화씨 온도 리스트 T를 입력받아서, 더 따듯한 날씨를 위해서는 며칠을 기다려야 하는지를 출력하라.

# input T = [73, 74, 75, 71, 69, 72, 76, 73]
# output = [1, 1, 4, 2, 1, 1, 0, 0]

# 현재의 온도 '인덱스'를 스택에 쌓으면서, 이전 보다 상승하는 지점이라면 스택을 pop 하고, pop한 값과 현재 값의 '인덱스 차이'를 구한다.

def solution(T):
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        # 현재 온도와 스택 값을 비교한다.
        while stack and cur > T[stack[-1]]: # top와 비교
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

input = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution(input))