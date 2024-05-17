def is_prime(n):
    for i in range(2, int(n**.5)+1):
        if n%i==0:return False
    return True

def main():
    a=open(0)
    ans=[]
    while (n:=int(next(a))) != -1:
        if is_prime(n) and n%10==3:ans.append(f'{n} YES')
        else:
            i,m=2,n
            while m!=1:
                if m%i==0:
                    if i%10!=3:ans.append(f'{n} NO');break
                    while m%i==0:m//=i
                i+=1
            if m==1:ans.append(f'{n} YES')
    print('\n'.join(ans))
main()