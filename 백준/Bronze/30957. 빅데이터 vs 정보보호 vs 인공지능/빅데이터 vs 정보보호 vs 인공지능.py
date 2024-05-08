d={}
input()
s=input()
for k in 'BSA': d[k] = s.count(k)
li=sorted([(k, v) for k, v in d.items()], key=lambda x: -x[1])
ans, m = li[0]
for k, v in li[1:]:
    if m==v: ans+=k
print(ans if ans!='BSA' else 'SCU')