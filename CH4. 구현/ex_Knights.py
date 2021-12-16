# 나이트는 2가지 이동방식을 가짐
# 수평으로 두칸 이동 후 수직으로 한칸
# 수직으로 두칸 이동 후 수평으로 한칸

# 나이트의 위치가 주어질 때 이동할 수 있는 경우의 수를 출력
# 판은 8x8 사이즈이고, 위치는 (a,2) 식으로 표현함

# 나이트의 현재 위치를 받는다.
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # 유니코드 값 반환

steps = [(-2,-1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향을 모두 테스트 해본다
result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    # 가능한 위치이면 카운트 증가
    if next_row >= 1 and next_col <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
        
print(result)