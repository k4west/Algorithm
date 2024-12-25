a = open(0)
for _ in range(int(next(a))):
    N, M, K = map(int, next(a).split())
    print(2*max(0, (N-2)//M)+1 if (M:=M*K-1) else 1-2*(N!=1))