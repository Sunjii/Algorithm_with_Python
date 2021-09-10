# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 2 ~ 9 까지 숫자가 주어질 때, 전화번호로 조합 가능한 모든 문자열을 출력하라.

'''
2 : a b c
3 : d e f
4 : g h i
...
9 : w x y z

input : 23
output : ['ab', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
'''

# 모든 조합을 탐색해야 한다.
# 최적화된 탐색을 위해 백트래킹을 쓸 수 있을 것이다.

def solution(digits):
    def dfs(index, path):
        # 백트래킹
        if len(path) == len(digits):
            answer.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                #print(i, j, path)
                dfs(i+1, path+j)

    # 예외처리
    if not digits:
        return []
    
    dic = {
        "2": "abc", "3": "def", "4":"ghi", "5":"jkl",
        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
    }
    answer = []
    dfs(0, "")

    return answer

input = "234"
print(solution(input))
