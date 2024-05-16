h,m=map(int,input().split(':'))
H,M=map(int,input().split(':'))
print((H-h-int((m:=M-m)<0))%24+(m)%60)