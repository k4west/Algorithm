M, N = map(int, open(0))
d = {i:1 for i in range(2, N+1)}
for n in range(2, int(N**.5)+1):
    if d[n]:
        for i in range(n**2, N+1, n): 
            d[i] = 0
li = [k for k, v in d.items() if v and k >= M]
if li: print(sum(li), li[0], sep='\n')
else: print('-1')