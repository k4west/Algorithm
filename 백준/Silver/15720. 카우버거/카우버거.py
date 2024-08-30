a,*b=open(0)
a=[*map(int,a.split())]
b=[*map(lambda x:sorted(map(int,x.split())), b)]
n=min(a)
t=sum(sum(b,[]))
k=sum([sum(j[:i-n]) for i, j in zip(a,b)])
print(t)
print((t-k)//10*9+k)