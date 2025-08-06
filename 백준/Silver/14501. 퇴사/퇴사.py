def bt(i, p):
    global max_p

    if max_p < p:
        max_p = p

    for j in range(i, N):
        tj, pj = TP[j]
        if j+tj <= N:
            bt(j+tj, p+pj)


N = int(input())
TP = [[*map(int, input().split())] for _ in range(N)]

max_p = 0
bt(0, 0)

print(max_p)