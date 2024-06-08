t=[]
for i in open(0).readlines():
    r,c=map(int,i.strip()[1:].split('C'))
    if r==c==0:break
    s=''
    while c:
        c-=1
        j=c%26
        s+=chr(j+65)
        c//=26
    t.append(f'{s[::-1]}{r}')
print('\n'.join(t))