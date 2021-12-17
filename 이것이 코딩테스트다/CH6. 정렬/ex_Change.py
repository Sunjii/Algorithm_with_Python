# 두 배열에서 원소를 교환한다
# 최대 K번 교환을 할 수 있고, 교환 결과 첫번째 배열의 원소 합이 최대가 되도록 한다
# 그 때의 합의 최대값을 출력하라


# 가장 작은 원소와 두번째 배열의 가장 큰 원소를 바꾼다
# k번 반복하면 된다

# input 처리
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 각 배열 정렬
a.sort()
b.sort(reverse=True)

for i in range(k):
    # a가 더 작은 경우 교환
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))