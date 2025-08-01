d = {'L': -1, 'R': 1}
L, N, T = map(int, input().split())
pos = []
for _ in range(N):
    S, C = input().split()
    pos.append([int(S), d[C]])

cnt = 0
for _ in range(T):              # T초 동안
    box = [[] for _ in range(L+1)]
    for i in range(N):          # 매초 위치 업데이트
        pos[i][0] += pos[i][1]
        s = pos[i][0]
        if s == 0 or s == L:    # 벽에 부딪히면 방향 전환
            pos[i][1] *= -1
        box[s].append(i)

    for li in box:              # 같은 위치에 있으면 공끼리 부딪힘 -> 방향 전환
        if len(li) == 2:
            cnt += 1
            for i in li:
                pos[i][1] *= -1

print(cnt)