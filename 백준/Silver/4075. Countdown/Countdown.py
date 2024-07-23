def f(r, j, d):
    if d==1:
         return len(r[j])
    t=0
    for k in r[j]:
        if k in r:
            t+=f(r, k, d-1)
    return t

a=open(0)
s=[]
for i in range(int(next(a))):
    t=[]
    n,d=map(int,next(a).split())
    r={}
    for _ in range(n):
        p,*c=next(a).split()
        r[p]=[j for j in c[1:]]
    for j in r:
        if g:=f(r, j, d):
            t.append((-g, j))
    t.sort()
    o=3
    w=[]
    p=float('-inf')
    for g, j in t:
        o-=1
        if o<0:
            if p<g:
                break
        p=g
        w.append(f'{j} {-g}')
    t=[f'Tree {i+1}:']+w
    s.append('\n'.join(t))
print('\n\n'.join(s))