def check(m, f, i, N, d=0):
    s = 0
    for p in range(N):
        if p == i:
            continue
        t = a[d+p]
        for k in range(25):
            if t[k] not in [m[k], f[k]]:
                break
        else:
            s += 1
    return s
    
MF, *a = open(0)
M, F = map(int, MF.split())
A = [[0] * F for _ in range(M)]
for i in range(M):
    m = a[i]
    for j in range(F):
        f = a[M+j]
        A[i][j] = check(m, f, i, M) + check(m, f, j, F, M)
print('\n'.join(' '.join(map(str, line)) for line in A))