N,*A=map(int,open(0).read().split())
print(2, int(N/2<sum(a%2 for a in A)))