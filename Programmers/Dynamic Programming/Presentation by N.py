def solution(N, number):
    s = [set() for x in range(8)] # 집합을 활용하여 중복 배제
    # s라는 리스트에는 8개의 집합이 담기게 된다.
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i)) # N이 5라면 5, 55, 555, 5555... 을 만드는 것
    
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
                    
    
    return answer