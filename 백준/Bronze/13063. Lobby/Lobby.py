t=[]
for i in open(0):
    n,m,k=map(int,i.split())
    if n==0:continue
    s=n//2+1-m
    p=n-m-k
    if s<=p:t.append(max(s,0))
    else:t.append(-1)
print('\n'.join(map(str,t)))