d=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
n,*b=open(0).read().split()
n=int(n)
b=list(map(list,b))
f=0
for i in range(n):
    for j in range(n):
        if b[i+n][j]=='x':
            if b[i][j]=='*':
                f=1
            cnt=0
            for di,dj in d:
                ni=i+di
                nj=j+dj
                if 0<=ni<n and 0<=nj<n:
                    if b[ni][nj]=='*':
                        cnt += 1
            b[i+n][j]=str(cnt)
if f:
    for i in range(n):
        for j in range(n):
            if b[i][j]=='*':
                b[i+n][j]='*'
for l in b[n:]:
    print("".join(l))