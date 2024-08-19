n,m,*a=map(int,open(0).read().split())
p=0
for i in range(m):
    p+=a[n+i];p+=a[p]
    if p>=n-1:break
print(i+1)