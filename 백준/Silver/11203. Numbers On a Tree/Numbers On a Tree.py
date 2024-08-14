a=open(0).read().split()
if len(a)==2:h,d=a
else:h,d=a[0],''
n=2**(int(h)+1)-1
k=0
for i in d:k=k*2+1+(i=='R')
print(n-k)