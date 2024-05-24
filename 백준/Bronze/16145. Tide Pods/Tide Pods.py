a=open(0)
ans=[]
t=0
for i in range(int(next(a))):
    if t==0:t,n=map(int,next(a).split())
    p=[map(int,next(a).split()) for _ in range(n)]
    *j,=map(int,next(a).split())
    if len(j) > t:t,n=j[-2:]
    else:t=n=0
    q=[]
    for k in p:
        *k,s=k
        q.append(s*sum(u==v==1 for u,v in zip(j,k)))
    q.sort()
    ans.append(f'Data Set {i+1}:\n{q[-1]-q[0]}\n')
print('\n'.join(ans))