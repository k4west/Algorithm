a,d,k=map(int,input().split())
k-=a
if k%d or k*d<0 or (k and abs(k)<abs(d)):print('X')
else:print(1+k//d)