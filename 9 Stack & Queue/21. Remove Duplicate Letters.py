# https://leetcode.com/problems/remove-duplicate-letters
# 중복된 문자만 제거해서 사전식 순서로 나열하라

# input : bcabc
# output : abc
# input : ebcabc
# output : eabc


# c b a c d c b c
# _ _ a c d c b c
# _ _ a c d _ b _
# ==> a c d b

# 각 문자의 개수를 카운팅하고, 스택에 문자를 하나씩 순서대로 집어 넣는다.
# 이 때 스택에 들어오는 문자에 대해서, 카운터가 0 이상, 즉 더 붙일 동일문자가 남아있다면, 스택에 쌓여있는 해당 문자를 없앤다.
# 또 이미 처리된 문자라면 (없앤 문자라면) 스킵한다.

# sol1) 스택
import collections
def removeDuplicateLetters(s):
    counter, stack = collections.Counter(s), []

    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # 스택이 비어있지 않으면서,
        # 현재 스택top문자가 개수여유가 있고, char가 top보다 앞서는 문자라면 스택에서 문자를 제거한다.
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)

    return ''.join(stack)

