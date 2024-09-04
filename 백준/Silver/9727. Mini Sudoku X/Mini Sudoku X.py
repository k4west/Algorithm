def sol(rows):
    rows = [*map(lambda x:[*map(int,x.split())],rows)]
    squ=[[] for _ in range(2)]
    if 6!=len(set([rows[i][i] for i in range(6)])):return 0
    if 6!=len(set([rows[i][5-i] for i in range(6)])):return 0
    for row in rows:
        if 6!=len(set(row)):return 0
        squ[0].extend(row[:3])
        squ[1].extend(row[3:])
        if len(squ[0])==6:
            for s in squ:
                if 6!=len(set(s)):return 0
            squ=[[] for _ in range(2)]
    for c in zip(*rows):
        if 6!=len(c):return 0
    return 1
n,*a=open(0)
print('\n'.join([f'Case#{i+1}: {sol(a[6*i:6*(i+1)])}' for i in range(int(n))]))