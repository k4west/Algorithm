d = ((0, 1), (1, 0),  (0, -1), (-1, 0))  # 오른쪽, 아래, 왼쪽, 위

ans = []
N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]

for r0 in range(N):
    flag = False
    r, c, direction = r0, 0, 0
    v = [[[0]*4 for _ in range(M)] for _ in range(N)]
    v[r][c][direction] = 1

    while True:
        step = graph[r][c]
        dr, dc = d[direction]
        nr, nc = r + dr * step, c + dc * step   # 별이 놓인 칸에 적힌 수만큼

        if 0 <= nr < N and 0 <= nc < M:
            direction = (direction + 1) % 4     # 시계 방향 90도.
            if v[nr][nc][direction]:
                flag = True
                break

            v[nr][nc][direction] = 1
            r, c = nr, nc

        else:
            break

    if flag:
        ans.append(r0+1)

if ans:
    print(len(ans))     # 올려둘 수 있는 칸 수
    print(" ".join(map(str, sorted(ans))))  # 몇 번째 행인지 공백을 사이에 두고 오름차순
else:
    print(0)
