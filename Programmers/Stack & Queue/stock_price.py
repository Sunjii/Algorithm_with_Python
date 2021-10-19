def solution(prices):
    # answer = [0] * len(prices)

    # brute force 방식
    # 배열의 시작에서 끝까지 비교해 나가면서 작아지면 계속 +1을 함
    # for i in range(len(prices)):
    #    for j in range(i+1, len(prices)):
    #        if prices[i] <= prices[j]:
    #            answer[i] += 1
    #        else:
    #            answer[i] += 1
    #            break

    # stack 활용
    # 가격을 stack에 하니씩 쌓는다. 다음 price가 크면 스택에 쌓고
    # 다음 가격이 작다면 pop를 한다.
    # pop의 개수가 answer가 된다.
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        # stack이 비어있으면
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # stack에 남은 것들을 pop한다
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
