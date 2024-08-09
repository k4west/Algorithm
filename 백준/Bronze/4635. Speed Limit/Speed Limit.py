a=open(0)
b=[]
while True:
    if (n:=int(next(a)))==-1:
        break
    p=m=0
    for _ in range(n):
        s,t=map(int,next(a).split())
        m+=s*(t-p)
        p=t
    b.append(f'{m} miles')
print('\n'.join(b))