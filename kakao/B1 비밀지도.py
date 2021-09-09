# input
# 1 <= n <= 16 : 한 변의 길이
# arr1, arr2 : 길이 n의 정수 배열. 각각 지도 1과 지도 2를 표현함

# output
# 총 길이가 n인 배열. 완성된 지도를 의미함

def solutions(n, arr1, arr2):
    result = []

    # arr1과 arr2의 요소 OR 연산을 한 것을 result에 넣는다.
    for i in range(n):
        result.append(bin(arr1[i] | arr2[i])[2:]
        .replace('1', '#')
        .replace('0', ' ')
        )

    return result

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solutions(5, arr1, arr2))
