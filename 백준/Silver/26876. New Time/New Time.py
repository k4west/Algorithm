a=[r-w for w, r in zip(map(int,input().split(':')), map(int,input().split(':')))]
print((a[0]-int(a[1]<0))%24+a[1]%60)