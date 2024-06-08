t=[]
for i in open(0).readlines():
    r,c=i.strip()[1:].split('C')
    if r==c=='0':break
    c=int(c);s=''
    while c:c-=1;j=c%26;s+=chr(j+65);c//=26
    t.append(s[::-1]+r)
print('\n'.join(t))