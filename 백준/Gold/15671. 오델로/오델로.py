def sol(r, c):    # 인접한 다른 색 찾기 -> 같은 방향으로 쭉 가다가 같은 색 발견
    li = []
    for dr, dc in d:
        flag = False
        tmp = []
        nr, nc = r + dr, c + dc
        while 0 <= nr < 6 and 0 <= nc < 6 and graph[nr][nc] == color[(i + j + 1) % 2]:
            flag = True
            tmp.append((nr, nc))
            nr += dr
            nc += dc
        if flag and 0 <= nr < 6 and 0 <= nc < 6 and graph[nr][nc] == color[(i + j) % 2]:
            li.extend(tmp)

    if li:
        li.append((r, c))
        for r, c in li:
            graph[r][c] = color[(i + j) % 2]
        return True
    else:
        return False


d = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1))
color = 'BW'
graph = [['.']*6 for _ in range(6)]
graph[2][2] = 'W'
graph[3][3] = 'W'
graph[2][3] = 'B'
graph[3][2] = 'B'

i = 0
for j in range(int(input())):
    p, q = map(int, input().split())
    if not sol(p-1, q-1):
        i += 1
        sol(p-1, q-1)

b = w = 0
for i in range(6):
    for j in range(6):
        k = graph[i][j]
        if k == 'B':
            b += 1
        elif k == 'W':
            w += 1

print("\n".join("".join(row) for row in graph))
if b > w:
    print("Black")
else:
    print("White")