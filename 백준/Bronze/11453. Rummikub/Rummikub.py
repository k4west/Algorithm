def check(tiles):
    d={'b':[0]*101,'g':[0]*101,'r':[0]*101,'y':[0]*101,'a':[set() for _ in range(101)]}
    for tile in tiles:
        v,c=int(tile[:-1]),tile[-1]
        d[c][v]=1
        d['a'][v].add(c)
    if max(map(len,d['a']))>=3:return True
    for i in range(1,99):
        if d['b'][i:i+3]==[1,1,1]:return True
        if d['g'][i:i+3]==[1,1,1]:return True
        if d['r'][i:i+3]==[1,1,1]:return True
        if d['y'][i:i+3]==[1,1,1]:return True
    return False
def main():
    a=open(0)
    t=[]
    for _ in range(int(next(a))):
        m=int(next(a))
        tiles=next(a).split()
        if m>2 and check(tiles):t.append('YES')
        else:t.append('NO')
    print('\n'.join(t))
if __name__=="__main__":
    main()