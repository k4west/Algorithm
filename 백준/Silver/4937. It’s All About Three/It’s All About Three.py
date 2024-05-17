def main():
    n=10**6
    p=[False, False]+[True]*(n-1)
    for i in range(2,int(n**.5)+1):
        if p[i]:
            for j in range(i*i,n+1,i):p[j]=False
    a=open(0)
    ans=[]
    while (i:=int(next(a))) != -1:
        j,f=i,True
        for k in range(2, i+1):
            if p[k] and j%k==0:
                if k%10 != 3:
                    ans.append(f'{i} NO')
                    f=False
                    break
                while j%k==0:
                    j//=k
            if j==1:break
        if f:ans.append(f'{i} YES')
    print('\n'.join(ans))
main()