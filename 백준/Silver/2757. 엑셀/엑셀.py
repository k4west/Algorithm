def f(c,s=''):
    while c:
        c-=1
        j=c%26
        s+=chr(j+65)
        c//=26
    return s[::-1]
t=[]
for i in open(0).readlines():
    r,c=i.strip()[1:].split('C')
    if r==c=='0':break
    t.append(f(int(c))+r)
print('\n'.join(t))