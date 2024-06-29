t=[]
for i in open(0):
    a,b=i.strip().split()
    if a==b=='0':
        exit(print(*t,sep='\n'))
    n=max(map(len,(a,b)))
    c=carry=0
    for x,y in zip(a.zfill(n)[::-1],b.zfill(n)[::-1]):
        if int(x)+int(y)+carry>9:
            c+=1
            carry=1
    t.append(c)