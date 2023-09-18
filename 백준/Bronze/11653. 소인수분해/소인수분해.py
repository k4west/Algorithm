N = int(input())
t = []
for n in range(2, int(N**.5)+1):
    while not N%n:
        t.append(n)
        N //= n
if t: print(*t, sep='\n')
if N!=1: print(N)