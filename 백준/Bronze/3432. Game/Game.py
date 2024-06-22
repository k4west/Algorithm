def main():
    w=[]
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
                if s*2==t[r][c]+t[r+2][c+2]: p[s=='B']=True
                if s*2==t[r][c+2]+t[r+2][c]: p[s=='B']=True
        
        a,b=map(int,p)
        w.append(['draw','A wins','B wins'][(a>b)+2*(a<b)])
    print('\n'.join(w))
main()