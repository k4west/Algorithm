def main():
    w=[]
    n,*m=open(0)
    for i in range(int(n)):
        t=m[i*5:(i+1)*5]
        p=[0,0]
        for j in range(5):
            r,c=t[j][2],t[2][j]
            if r*3 in t[j]: p[r=='B']=1
            if c*3 in ''.join([k[j] for k in t]): p[c=='B']=1
            if j<3:
                for k in range(3):
                    s = t[j+1][k+1]
                    if s*2==t[j][k]+t[j+2][k+2]: p[s=='B']=1
                    if s*2==t[j][k+2]+t[j+2][k]: p[s=='B']=1
        a,b=p
        w.append(['draw','A wins','B wins'][(a>b)+2*(a<b)])
    print('\n'.join(w))
main()