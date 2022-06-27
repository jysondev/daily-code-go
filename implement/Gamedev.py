from glob import glob


n, m = map(int, input().split())

# 컴프리헨션 - 방문위치 저장
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
# map
for i in range(n):
    array.append(list(map(int, input().split())))

# 동서남북정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
ture_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x ,y = nx, ny
        count += 1
        ture_time = 0
        continue
    else:
        ture_time+=1
    
    if ture_time == 4:
        nx, ny = x-dx[direction], y-dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        ture_time = 0

print(count)

