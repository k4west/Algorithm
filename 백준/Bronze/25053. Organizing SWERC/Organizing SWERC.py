a=open(0)
t=[]
for _ in range(int(next(a))):
    n=int(next(a));s=[0]*11
    for _ in range(n):
        b,d=map(int,next(a).split())
        if s[d]<b:s[d]=b
    if s.count(0)>1:t.append('MOREPROBLEMS')
    else:t.append(str(sum(s)))
print('\n'.join(t))