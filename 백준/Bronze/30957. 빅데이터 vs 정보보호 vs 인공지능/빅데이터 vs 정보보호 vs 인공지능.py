d={'B':0, 'S':0 ,'A':0}
o={'B':0, 'S':1, 'A':2}
a=open(0)
next(a)
for s in next(a).rstrip():
    d[s] += 1
li=sorted([(k, v) for k, v in d.items()], key=lambda x: (-x[1], o[x[0]]))
ans=''
m=0
for k, v in li:
    if m<=v:
        ans+=k
        m=v
if ans=='BSA':
    ans='SCU'
print(ans)