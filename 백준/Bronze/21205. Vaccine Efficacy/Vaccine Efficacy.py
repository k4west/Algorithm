a=open(0).readlines()[1:]
d=[[0,0,0],[0,0,0]]
c=[0,0]
for i in a:
    i=i.strip()
    j=i[0]=='Y'
    c[j]+=1
    for k in range(3):
        if i[k+1]=='Y':d[j][k] += 1
for i, j in zip(*d):
    if i/c[0] <= j/c[1]:print('Not Effective')
    else:print(f'{100-(100*j*c[0])/(i*c[1]):.6f}')