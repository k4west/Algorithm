a=open(0)
t=[]
for i in range(int(next(a))):
    t.append(f'Case #{i+1}:')
    n=int(next(a))
    s=[next(a).strip().upper() for _ in range(n)]
    if n==1:
        t.append('""')
        continue
    for j in range(n):
        b=''
        p=s[j]
        for k in range(1, len(p)+1):
            for l in range(len(p)-k+1):
                c=p[l:l+k]
                f=False
                for m in range(n):
                    if j==m:continue
                    if c in s[m]:
                        f=True
                        break
                if not f:
                    if b:
                        b=min(b,c) #
                    else:
                        b=c
            if b:
                break
        if b:
            t.append(f'"{b}"')
        else:
            t.append(':(')
print('\n'.join(t))