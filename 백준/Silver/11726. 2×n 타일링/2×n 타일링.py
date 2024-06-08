m=10007
l=[1,1]
for _ in range(int(input())-1):l.append((l[-1]+l[-2])%m)
print(l[-1])