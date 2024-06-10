a=open(0)
t=[]
for _ in range(int(next(a))):
    A,B,T=map(int,next(a).split())
    while B:A,B=B,A%B
    t.append(T//A)
print(*t,sep='\n')