N,M=map(int,input().split())
if N-1<=M<=2*N-3:
    t=[]
    for i in range(1,N):
        t.append(f'{i} {i+1}')
    for i in range(1,M-N+2):
        t.append(f'{i} {i+2}')
    print('\n'.join(t))
else:
    print(-1)
