m=set(range(1,7))
def check(li):
    return set(li)==m
t=[]
n,*a=open(0)
for i in range(int(n)):
    p=1
    col=[[] for _ in range(6)]
    dia=[[] for _ in range(2)]
    squ=[[] for _ in range(2)]
    for r,row in enumerate(map(lambda x:[*map(int,x.split())],a[6*i:6*(i+1)])):
        if not check(row):p=0;break
        squ[0].extend(row[:3])
        squ[1].extend(row[3:])
        if len(squ[0])==6:
            for s in squ:
                if not check(s):p=0;break
            if not p:break
            squ=[[] for _ in range(2)]
        for j,k in enumerate(row):
            col[j].append(k)
            if r==j:dia[0].append(k)
            if r+j==5:dia[1].append(k)
    for c in col:
        if not check(c):p=0;break
    for d in dia:
        if not check(d):p=0;break
    t.append(f'Case#{i+1}: {p}')
print('\n'.join(t))