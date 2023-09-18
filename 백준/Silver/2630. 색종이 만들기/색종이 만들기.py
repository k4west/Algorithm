def f(N, A):
    global wb
    s = sum(sum(A, []))
    if s == 0: wb[0] += 1
    elif s == N**2: wb[1] += 1
    else:
        M = N//2
        f(M, [i[:M] for i in A[:M]])
        f(M, [i[M:] for i in A[:M]])
        f(M, [i[:M] for i in A[M:]])
        f(M, [i[M:] for i in A[M:]])
    return

a = open(0)
N = int(next(a))
A = [list(map(int, i.split())) for i in a]
wb = [0, 0]
f(N, A)
print(*wb, sep='\n')