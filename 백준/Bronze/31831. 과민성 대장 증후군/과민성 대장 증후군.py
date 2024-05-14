a=open(0)
N,M=map(int,next(a).split())
s=d=0
for m in map(int,next(a).split()):
    if (s:=max(s+m,0))>=M:d+=1
print(d)