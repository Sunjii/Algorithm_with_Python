# 이름 성적 순으로 입력 데이터가 들어온다
# 성적 낮은순으로 정렬
# 개수는 100,000개 까지 입력된다

import time
start_t = time.time()

n = int(input())
arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

# 정렬
arr = sorted(arr, key=lambda stud:stud[1])
for stu in arr:
    print(stu[0], end=' ')

end_t = time.time()
print(end_t - start_t)