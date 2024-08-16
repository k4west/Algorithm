T,*a=open(0)
r=[]
for i in range(int(T)):
    K,*grids=a[i*13:(i+1)*13]
    K=int(K)
    w=[sorted(set(col[:6])&set(col[6:12])) for col in zip(*grids)]
    c=[len(j) for j in w]
    n=1
    for j in c:
        n*=j
    if n==0 or n<K:
        t='NO'
    else:
        t=''
        for j in range(5):
            n//=c[j]
            idx=0
            while True:
                if n*(idx+1)<K:
                    idx+=1
                else:
                    break
            t+=w[j][idx]
            K-=n*idx
    r.append(t)
print('\n'.join(r))