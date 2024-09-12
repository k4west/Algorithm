def check(s):
    d={'b':[0]*101,'g':[0]*101,'r':[0]*101,'y':[0]*101,'a':[set() for _ in range(101)]}
    for i in s:v,c=int(i[:-1]),i[-1];d[c][v]=1;d['a'][v].add(c)
    if max(map(len,d['a']))>=3:return True
    for i in range(1,99):
        for j in 'bgry':
            if d[j][i:i+3]==[1,1,1]:return True
    return False
a=open(0)
for _ in range(int(next(a))):m=int(next(a));s=next(a).split();print('YNEOS'[m<3 or not check(s)::2])