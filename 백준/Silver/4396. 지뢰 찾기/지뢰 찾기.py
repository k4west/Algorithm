d=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
n,*b=open(0).read().split()
n=int(n)
b=list(map(list,b))
f=0
for i in range(n):
    for j in range(n):
        if b[i+n][j]=='x':
            if b[i][j]=='*':f=1
            c=0
            for di,dj in d:
                if 0<=(ni:=i+di)<n and 0<=(nj:=j+dj)<n and b[ni][nj]=='*':c += 1
            b[i+n][j]=str(c)
if f:
    for i in range(n):
        for j in range(n):
            if b[i][j]=='*':b[i+n][j]='*'
for l in b[n:]:print("".join(l))