n,m,*a=map(int,open(0).read().split())
p=1
for i in range(m):
    p+=a[n+i]
    p+=a[p-1]
    if p>=n:
        break
print(i+1)