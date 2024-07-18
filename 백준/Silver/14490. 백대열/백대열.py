n,m=map(int,input().split(':'))
a,b=n,m
while b:
    a,b=b,a%b
print(f'{n//a}:{m//a}')