'''
1S2D*3T // 1^1 + 2^2 *2 + 3^3

1D 2S# 10S // 1^2 + 2^1 *(-1) + 10^1

0~10
D ^1, S ^2, T ^3
* : 이전값과 그 이전값 x2
# : 현재값 -1배



'''


def solution(dartResult):
    nums = []

    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
        elif s == 'D':
            nums[-1] **= 2
        elif s == 'T':
            nums[-1] **= 3
        elif s == '*':
            nums[-1] *= 2
            if len(nums) > 1:
                nums[-2] *= 2
        elif s == '#':
            nums[-1] *= -1
        elif s == '0':
            nums[-1] *= 10
        else: # 숫자인 경우
            nums.append(int(s))
            # 10인 경우는??
        print(nums)

    result = 0
    for n in nums:
        result += n

    return result

input1 = '1D2S3T*'
input2 = '1T2D3D#'
input3 = '1D#2S*3S'
inputA = '1D2S#10S'
print(solution(input1), solution(input2), solution(input3))
print(solution(inputA))