def main():
    a=open(0)
    for i in range(int(next(a))):
        print(f'Case #{i+1}:');n=int(next(a));s=[next(a).strip().upper() for _ in range(n)]
        if n==1:print('""');continue
        for j in range(n):
            b=[];p=s[j]
            for k in range(1,len(p)+1):
                for l in range(len(p)-k+1):
                    c=p[l:l+k];f=False
                    for m in range(n):
                        if j==m:continue
                        if c in s[m]:f=True;break
                    if not f:b.append(c)
                if b:break
            if b:print(f'"{min(b)}"')
            else:print(':(')
main()