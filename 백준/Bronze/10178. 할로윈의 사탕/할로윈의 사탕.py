n,*a=open(0)
t=[]
for i in a:
    c,v=map(int,i.split())
    t.append(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')
print('\n'.join(t))