a,b,c,d,e,f=map(int,open(0).read().split())
if -1 in (i:=(a, e, f)) and (f==0 or i.count(-1)==1):
    if f==0:a=e=f
    elif a==-1:a=f-e
    elif e==-1:e=f-a
    else:f=a+e
if -1 in (i:=(d, b, c)) and (c==0 or i.count(-1)==1):
    if c==0:d=b=c
    elif d==-1:d=c-b
    elif b==-1:b=c-d
    else:c=d+b
print(f'{a} {b} {c}\n{d} {e} {f}')