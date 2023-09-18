def f(N, A):
    s = sum(sum(A, []))
    if s == 0: w, b = 1, 0
    elif s == N**2: w, b = 0, 1
    else:
        M = N//2
        A0, A1, A2, A3 = [i[:M] for i in A[:M]], [i[M:] for i in A[:M]], [i[:M] for i in A[M:]], [i[M:] for i in A[M:]]
        t0, t1, t2, t3 = f(M, A0), f(M, A1), f(M, A2), f(M, A3)
        w, b = [sum(j) for j in zip(t0, t1, t2, t3)]
    return w, b

a = open(0)
N = int(next(a))
A = [list(map(int, i.split())) for i in a]
w, b = f(N, A)
print(w)
print(b)