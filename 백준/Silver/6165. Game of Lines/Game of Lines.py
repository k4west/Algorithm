n,*a=open(0)
n=int(n)
a=[[*map(float,i.split())] for i in a]
f=False
s=set()
for i in range(n):
    x0,y0=a[i]
    for j in range(i+1,n):
        x1,y1=a[j]
        if x1==x0:f=True
        else:
            s.add((y1-y0)/(x1-x0))
print(len(s)+f)