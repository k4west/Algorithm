a = open(0)
next(a)
c=sorted(map(int, next(a).split()))
s = 0
p = -1
for n in c:
    if p+1!=n:s+=n
    p=n
print(s)
