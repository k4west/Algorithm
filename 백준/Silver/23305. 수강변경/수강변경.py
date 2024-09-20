n,a,b=open(0)
d={}
for i in map(int,b.split()):
    d[i]=d.get(i,0)+1
for i in map(int,a.split()):
    if d.get(i, 0):
        d[i] -= 1
print(sum(d.values()))