def f(M,N):
    li = [0,0]+[1]*(N-1)
    for n in range(2, int(N**.5)+1):
        if li[n]:
            for i in range(n**2, N+1, n): li[i] = 0
    return [i for i in range(M, N+1) if li[i]]
M, N = map(int, open(0))
s = f(M, N)
if s: print(sum(s), s[0], sep='\n')
else: print('-1')