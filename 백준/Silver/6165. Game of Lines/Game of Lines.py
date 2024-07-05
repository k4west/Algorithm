n,*a=map(float,open(0).read().split())
n=int(n)
f=False
s=set()
for i in range(n):
    x0,y0=a[2*i:2*(i+1)]
    for j in range(i+1,n):
        x1,y1=a[2*j:2*(j+1)]
        if x1==x0:f=True
        else:s.add((y1-y0)/(x1-x0))
print(len(s)+f)