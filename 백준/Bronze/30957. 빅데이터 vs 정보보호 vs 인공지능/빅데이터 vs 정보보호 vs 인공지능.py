d={}
a=open(0)
next(a)
s=next(a)
for k in 'BSA':
    d[k] = s.count(k)
li=sorted([(k, v) for k, v in d.items()], key=lambda x: -x[1])
ans=''
m=0
for k, v in li:
    if m<=v:
        ans+=k
        m=v
if ans=='BSA':
    ans='SCU'
print(ans)