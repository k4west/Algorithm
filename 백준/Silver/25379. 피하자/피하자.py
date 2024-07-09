_,*a=map(lambda x: float(x)%2, open(0).read().split())
n=len(a)
r=l=s=t=0
for i, j in zip(a, a[::-1]):
    if i:s+=1
    else:r+=s
    if j:t+=1
    else:l+=t
print(min(r,l))