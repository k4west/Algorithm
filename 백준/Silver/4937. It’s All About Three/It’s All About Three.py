def main():
    n=10**6
    p=[False, False]+[True]*(n-1)
    for i in range(2,int(n**.5)+1):
        if p[i]:
            for j in range(i*i,n+1,i):p[j]=False
    a=open(0)
    ans=[]
    while (i:=int(next(a))) != -1:
        j=i
        tmp=[False]*10
        for k in range(2, i+1):
            if p[k]:
                while j%k==0:
                    j//=k
                    tmp[k%10]=True
            if j==1:break
        if [i for i in range(10) if tmp[i]] == [3]:ans.append(f'{i} YES')
        else:ans.append(f'{i} NO')
    print('\n'.join(ans))
main()