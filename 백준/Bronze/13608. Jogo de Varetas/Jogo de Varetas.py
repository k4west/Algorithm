a=open(0)
s=[]
while n:=int(next(a)):
    t=0
    for _ in range(n):
        c,v=map(int,next(a).split())
        t+=v//2
    s.append(t//2)
print('\n'.join(map(str,s)))