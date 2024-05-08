d={}
a=open(0)
next(a)
s=next(a)
for k in 'BSA':
    d[k] = s.count(k)
li=sorted([(k, v) for k, v in d.items()], key=lambda x: -x[1])
ans, m = li[0]
for k, v in li[1:]:
    if m==v: ans+=k
if ans=='BSA':
    ans='SCU'
print(ans)