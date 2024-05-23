n=[]
for l in open(0).readlines()[1:]:
    a,b=map(int, l.split())
    n.append(['TAK','NIE'][bool(b%a)])
print('\n'.join(n))