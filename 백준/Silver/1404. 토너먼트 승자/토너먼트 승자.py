import sys
P=[0]*64
prev=i=0
for k,p in enumerate(map(int, sys.stdin.readline().split()),1):
    j=k-prev
    P[i*8+j],P[j*8+i]=p/100,1-p/100
    if j==7:
        i+=1
        prev=k-i
tmp=[]
for n in range(1,9):
    if n%2:
        a,b=(n+1)%4+(n//4)*4,(n+2)%4+(n//4)*4
        tmp.append(P[(n-1)*8+n]*(P[(n-1)*8+a]*P[a*8+b]+P[(n-1)*8+b]*P[b*8+a]))
    else:
        a,b=n%4+((n-1)//4)*4,(n+1)%4+((n-1)//4)*4
        tmp.append(P[(n-1)*8+(n-2)]*(P[(n-1)*8+a]*P[a*8+b]+P[(n-1)*8+b]*P[b*8+a]))
ans=[]
for n in range(1,9):
    if (n+3)%8//4:ans.append(tmp[n-1]*sum(P[(n-1)*8+i]*tmp[i] for i in range(4,8)))
    else:ans.append(tmp[n-1]*sum(P[(n-1)*8+i]*tmp[i] for i in range(4)))
print(" ".join(map(lambda x:f"{x:.13f}",ans)))