_,*a=open(0)
t=[]
for i in a:
    j,*b=map(int,i.split())
    c=sum([sum([1 for q in b[:k] if q>p]) for k,p in enumerate(b)])
    t.append(f'{j} {c}')
print('\n'.join(t))