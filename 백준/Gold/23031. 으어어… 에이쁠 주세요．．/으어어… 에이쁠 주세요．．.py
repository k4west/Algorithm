def move(r, c):
    dr, dc = move_d[direction]
    nr, nc = r+dr, c+dc
    if 0 <= nr < N and 0 <= nc < N:
        return nr, nc
    return r, c


def zombie_move(r, c, idx):
    dr, dc = move_d[idx]
    nr, nc = r+dr, c+dc
    if 0 <= nr < N and 0 <= nc < N:
        return nr, nc, idx
    return r, c, (idx+2) % 4


def switch_on(r, c):
    if graph[r][c] == "S":
        lights[r][c] = True
        for dr, dc in switch_d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                lights[nr][nc] = True

    return lights[r][c]


def check(pos, light_on):
    if not light_on:
        for k in range(z):
            if zombies[k][:2] == pos:
                return True

    for k in range(z):
        zombies[k] = zombie_move(*zombies[k])

    if not light_on:
        for k in range(z):
            if zombies[k][:2] == pos:
                return True

    return False


options = ["Phew...", "Aaaaaah!"]
move_d = ((0, 1), (1, 0), (0, -1), (-1, 0))      # 0: 동, 1: 남, 2: 서, 3: 북
switch_d = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
direction = 1    # 아리와 학생 좀비들은 모두 아래 방향


z, zombies = 0, []
N = int(input())
A = input()
graph = [list(input()) for _ in range(N)]
lights = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'Z':
            zombies.append((i, j, 1))
            graph[i][j] = 'O'
            z += 1

i = j = 0
flag = False

if z:
    for a in A:
        if a == "F":
            i, j = move(i, j)
        elif a == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

        flag = check((i, j), switch_on(i, j))
        if flag:
            break

print(options[flag])
