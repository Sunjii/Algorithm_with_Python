# 찾는 수자의 처음 위치와 마지막 위치를 찾으면 된다.

# 입력 처리
n, target = map(int, input().split())
arr = list(map(int, input().split()))

# 첫 위치 찾기
def first(arr, target, s, e):
    if s > e:
        return None
    
    mid = (s+e)//2
    # 가장 왼쪽 위치인지
    # 1 t t t 3 ...
    if (mid == 0 or target > arr[mid -1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        # 왼쪽 확인
        return first(arr, target, s, mid-1)
    else:
        # 오른쪽 확인
        return first(arr, target, mid+1, e)

# 마지막 위치 찾기
def last(arr, target, s, e):
    if s > e:
        return None
    mid = (s+e)//2
    # 가장 오른쪽 위치인지
    # 1 t t t 3 ...
    if (mid == n-1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        # 왼쪽 확인
        return last(arr, target, s, mid-1)
    else:
        # 오른쪽 확인
        return last(arr, target, mid+1, e)
    
# 개수 계산
def count_by(arr, x):
    n = len(arr)
    a = first(arr, x, 0, n-1)
    if a == None:
        return 0
    b = last(arr, x, 0, n-1)
    return b-a+1

count = count_by(arr, target)
print(count)
            