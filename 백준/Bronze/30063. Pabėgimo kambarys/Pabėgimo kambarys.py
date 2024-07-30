t='RAKTAS'
n,s=open(0)
for i in range(int(n)):
    t=t.replace(s[i],'',1)
    if not t:
        break
print(i+1)