N,M,T,K=map(int,input().split())
s=0
while True:
    if (N:=N-M)>0:s+=M*K
    else:s+=(N+M)*K;break
    if (K:=K-T)<=0:break
print(s)