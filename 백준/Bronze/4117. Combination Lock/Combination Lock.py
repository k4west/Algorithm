t = []
for i in open(0):
    N,a,b,c=map(int,i.split())
    if N:
        t.append(4*N-1+(b-a)%N+(b-c)%N)
print(*t,sep='\n')