a = open(0)
print(int(max(i*j for i, j in zip(range(int(next(a)),0,-1), sorted(map(float, a.read().split()))))))