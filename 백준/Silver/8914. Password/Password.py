T,*a=open(0)
r=[]
for i in range(int(T)):
    K,*grids=a[i*13:(i+1)*13]
    K=int(K)
    w=[sorted(set(col[:6])&set(col[6:12])) for col in zip(*grids)]
    c=[len(j) for j in w]
    n=1;t=''
    for j in c:n*=j
    if n==0 or n<K:t='NO'
    else:
        for j in range(5):
            n//=c[j];k=0
            while True:
                if n*(k+1)<K:k+=1
                else:break
            t+=w[j][k];K-=n*k
    r.append(t)
print('\n'.join(r))