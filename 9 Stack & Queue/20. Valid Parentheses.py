# https://leetcode.com/problems/valid-parentheses/
# 괄호로 된 입력 값이 올바른지 판별하라

# input : ()[]{}
# output : true

def isValid(s:str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in table:
            stack.append(char) # 시작하는 문자가 온다면 스택에 넣고 
        elif not stack or table[char] != stack.pop():
            return False
        
    return len(stack) == 0

input = "()[]{}"
print(isValid(input))