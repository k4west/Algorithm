a=open(0)
K=int(next(a))
C=int(next(a))
t = []
for _ in range(C):
    M, N = map(int, next(a).split())
    F = True
    if M < N:
        if N-(M+K-N) > 1:
            F = False
    elif M > N:
        if M-(N+K-M) > 2:
            F = False
    t.append('01'[F])
print('\n'.join(t))