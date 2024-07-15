N,Q,*a=map(int, open(0).read().split())
n,q=a[:N],a[N:]
t=[[i]*j for i,j in enumerate(n,1)]
t=sum(t,[])
print('\n'.join(map(str,[t[i] for i in q])))