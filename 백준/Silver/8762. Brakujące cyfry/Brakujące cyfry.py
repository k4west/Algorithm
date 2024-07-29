a=open(0)
ans=[]
for _ in range(int(next(a))):
    tmp=[]
    for _ in range(int(next(a))):
        A,B=next(a).strip().split()
        if 'x' in A:
            B=int(B)
            t=A.index('x')
            for i in '0123456789'[not t:]:
                C=A.replace('x',i)
                if int(C)%B==0:
                    break
        else:
            A=int(A)
            t=B.index('x')
            for i in '0123456789'[not t:]:
                C=B.replace('x',i)
                if A%int(C)==0:
                    break
        tmp.append(i)
    ans.append(''.join(tmp))
print('\n'.join(ans))