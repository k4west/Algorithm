h,m=map(int,input().split(':'))
H,M=map(int,input().split(':'))
print((H-h-int(m>M))%24+(M-m)%60)