a=open(0)
t=[]
i=0
nl='\n'
while n:=int(next(a)):
    f=''
    u,r,d,l=[],[],[],[]
    x,y=map(int,next(a).split())
    x0,y0=x,y
    for _ in range(n-1):
        x1,y1=map(int,next(a).split())
        if x0==x1:
            if y0<y1:u.append(x0)
            else:d.append(x0)
        else:
            if x0<x1:r.append(y0)
            else:l.append(y0)
        x0,y0=x1,y1
    x1,y1=x,y
    if x0==x1:
        if y0<y1:u.append(x0)
        else:d.append(x0)
    else:
        if x0<x1:r.append(y0)
        else:l.append(y0)
    if (min(d)<max(u))|(min(r)<max(l)):f='im'
    t.append(f'Floor #{(i:=i+1)}{nl}Surveillance is {f}possible.')
print('\n\n'.join(t))