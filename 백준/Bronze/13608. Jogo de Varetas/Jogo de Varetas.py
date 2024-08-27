a=open(0)
while n:=int(next(a)):print(sum((int(next(a).split()[1])//2 for _ in range(n)))//2)