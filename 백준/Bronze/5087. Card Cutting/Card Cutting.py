a=open(0)
s=[]
for i in a:
    if i[0] == '#':
        break
    c=t=0
    for j in i[:-2].split():
        if j in 'A13579':
            c+=1
        else:
            t+=1
    s.append(['Draw', 'Cheryl', 'Tania'][(c>t)-(c<t)])
print('\n'.join(s))