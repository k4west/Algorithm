n,*a=open(0)
for i in a:
    c,v=map(int,i.split())
    print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')
