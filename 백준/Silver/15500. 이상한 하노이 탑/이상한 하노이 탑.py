n=int(input())
p=[[],[*map(int,input().split())],[],[]]
u=1
v=2
a=[]
while n:
    f=False
    if not p[u]:u,v=v,u
    for _ in range(len(p[u])):
        if (j:=p[u].pop())==n:a.append(f'{u} 3');n-=1;break
        if j == n-1:f=True
        p[v].append(j)
        a.append(f'{u} {v}')
    if f:u,v=v,u
print(len(a))
print('\n'.join(a))