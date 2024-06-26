N,_,*a=open(0)
N=int(N)
l=[False]*N
m=0
c=0
for i in map(int,a):
    for j in range(i-1,N,i):
        l[j]=not l[j]
        c+=[-1,1][l[j]]
    if m<c:m=c
    if m==N:break
print(m)