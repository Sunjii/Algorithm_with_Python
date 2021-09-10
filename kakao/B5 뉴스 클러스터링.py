'''
자카드 유사도 : 교집합 / 합집합



'''
import re
import collections

def solution(str1, str2):
    jakad = 0

    # 각 문자열을 집합화
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1)-1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower())
    ]
    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2)-1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]
    print(str1s, str2s)

    # 교집합 계산
    inter = sum(
        (collections.Counter(str1s) & collections.Counter(str2s)).values()
        )
    
    # 합집합 계산
    union = sum(
        (collections.Counter(str1s) | collections.Counter(str2s)).values()
    )

    # jakad 유사도 계산
    jakad = 1 if union == 0 else inter/union

    return int(jakad * 65536)


input1 = "FRANCE"
input2 = "FRENCH"

print(solution(input1,input2))