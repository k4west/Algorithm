n,*a=map(int,open(0).read().split())
m=10**6+1
a=sorted([a[2*i:2*i+2] for i in range(n)])
for i in range(n-1):
    if a[i][1]!=a[i+1][1]:
        t=a[i+1][0]-a[i][0]
        if m>t:
            m=t
prev,c=a[0]
for x,s in a[1:]:
    if s and prev+m<=x:
        c+=1
    prev=x
print(c)