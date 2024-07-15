N,Q,*a=map(int, open(0).read().split())
n,q=a[:N],a[N:]
t=[]
for i,j in enumerate(n,1):
    for _ in range(j):t.append(i)
print('\n'.join(map(str,[t[i] for i in q])))