def gcd(a,b):
    while b:a,b=b,a%b
    return a

a=open(0)
t=[]
for _ in range(int(next(a))):
    A,B,T=map(int,next(a).split())
    t.append(T//gcd(A,B))
print(*t,sep='\n')