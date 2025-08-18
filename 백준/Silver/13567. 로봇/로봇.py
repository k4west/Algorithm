def turn(i):
    if i:   # TURN 1: 오른쪽으로 90도 회전: 동남서북
        return (direction+1) % 4
    else:   # TURN 0: 왼쪽으로 90도 회전: 동북서남
        return (direction-1) % 4


def move(i):
    dr, dc = d[direction]
    nr, nc = r+dr*i, c+dc*i
    if 0 <= nr < M and 0 <= nc < M:
        return nr, nc
    return -1, -1


d = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 동남서북
direction = r = c = 0   # 처음에 로봇은 (0, 0)에 위치해 있고, 동쪽 방향을 향하고 있다.
flag = False

M, n = map(int, input().split())
for _ in range(n):
    order, j = input().split()
    if order == "MOVE":
        r, c = move(int(j))
        if r == -1:     # 일련의 명령어 열을 이루는 각 명령어가 모두 유효하다면, 이 명령어 열을 유효하다고 한다.
            flag = True
            break
    else:
        direction = turn(int(j))

if flag:
    print(-1)
else:
    print(c, r)
