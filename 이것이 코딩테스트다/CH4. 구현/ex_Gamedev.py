'''
방향
0: N
1: E
2: S
3: W

1 : 바다, 0 육지
'''
# n x m 입력
n, m = map(int, input().split())
# map 초기화
d = [[0]* m for _ in range(n)]
# 초기 x,y 좌표 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 초기 위치는 방문처리함

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 4방위 정의 NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽 회전 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        

# 시뮬레이션
count = 1
turn_time = 0

while True:
    # 왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 칸이면 이동한다
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 4 방향 전부 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 이동 가능하면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            # 더는 이동 못 함. 정지
            break
        turn_time = 0

print(count)