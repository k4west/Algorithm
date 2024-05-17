import sys
def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if n%i==0:return False
    return True
ans=[]
for n in map(int, sys.stdin):
    if n==-1:print('\n'.join(ans))
    elif is_prime(n) and n%10==3:ans.append(f'{n} YES')
    else:
        m,f=n,True
        for i in range(2, int(n**.5)+1):
            if m%i==0:
                if i%10!=3:ans.append(f'{n} NO');f=False;break
                while m%i==0:m//=i
        if f:
            if m==1 or m%10==3:ans.append(f'{n} YES')
            else: ans.append(f'{n} NO')