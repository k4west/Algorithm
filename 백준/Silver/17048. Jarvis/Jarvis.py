from collections import Counter
N,A,B=open(0)
d=Counter(int(a)-int(b) for a,b in zip(A.strip().split(),B.strip().split()))
print(max(d.values()))