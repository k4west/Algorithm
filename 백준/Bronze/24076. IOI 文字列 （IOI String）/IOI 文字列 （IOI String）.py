n = int(input())
print(sum(i!=j for i, j in zip(input(), ('IO'*((n+1)//2))[:n])))