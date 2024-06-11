h,m=map(int,input().split(':'))
n=int(input())
while True:
    if not m:n-=h
    elif not m%15:n-=1
    if n<1:break
    m=(m+1)%60
    if not m:h+=1
    if h>12:h=1
print(f'{h:02d}:{m:02d}')