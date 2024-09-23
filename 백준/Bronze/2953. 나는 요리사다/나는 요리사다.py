n=s=0
for j,k in enumerate([sum(map(int, i.split())) for i in open(0)], 1):
    if s<k:n,s=j,k
print(n,s)