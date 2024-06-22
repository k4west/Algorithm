n,*m=open(0)
for i in range(int(n)):
    t=m[i*5:(i+1)*5]
    p=[False,False]

    for j in range(5):
        r,c=t[j][2],t[2][j]
        if r*3 in t[j]: p[r=='B']=True
        if c*3 in ''.join([k[j] for k in t]): p[c=='B']=True

    for r in range(3):
        for c in range(3):
            s = t[r+1][c+1]
            v = t[r][c]+s+t[r+2][c+2]
            if s*3==v: p[s=='B']=True
            v = t[r][c+2]+s+t[r+2][c]
            if s*3==v: p[s=='B']=True
    
    a,b=map(int,p)
    print(['draw','A wins','B wins'][(a>b)+2*(a<b)])