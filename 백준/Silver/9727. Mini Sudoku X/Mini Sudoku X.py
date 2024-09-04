def check(li):
    return len(set(li))==6
def sol(rows):
    col=[[] for _ in range(6)]
    dia=[[] for _ in range(2)]
    squ=[[] for _ in range(2)]
    for r,row in enumerate(map(lambda x:[*map(int,x.split())],rows)):
        if not check(row):return 0
        squ[0].extend(row[:3])
        squ[1].extend(row[3:])
        if len(squ[0])==6:
            for s in squ:
                if not check(s):return 0
            squ=[[] for _ in range(2)]
        for j,k in enumerate(row):
            col[j].append(k)
            if r==j:dia[0].append(k)
            if r+j==5:dia[1].append(k)
    for c in col:
        if not check(c):return 0
    for d in dia:
        if not check(d):return 0
    return 1
n,*a=open(0)
print('\n'.join([f'Case#{i+1}: {sol(a[6*i:6*(i+1)])}' for i in range(int(n))]))