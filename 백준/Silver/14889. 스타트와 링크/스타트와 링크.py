def get_diff(li):
    team_a = [i for i, j in enumerate(li) if j]
    team_b = [i for i, j in enumerate(li) if not j]

    score_a = score_b = 0
    for i in range(M):
        for j in range(i + 1, M):
            score_a += S[team_a[i]][team_a[j]]
            score_b += S[team_b[i]][team_b[j]]

    return abs(score_a - score_b)


def bt(depth, s):
    global diff

    if depth == M:
        tmp = get_diff(team)
        if diff > tmp:
            diff = tmp
        return

    for i in range(s, N):
        if not team[i]:
            team[i] = 1
            bt(depth+1, i+1)
            team[i] = 0


N = int(input())
S = [[*map(int, input().split())] for _ in range(N)]
team = [0]*N

for r in range(N):
    for c in range(r+1, N):
        S[r][c] = S[c][r] = S[r][c] + S[c][r]

M = N//2
diff = 40000

team[0] = 1
bt(1, 1)
print(diff)
