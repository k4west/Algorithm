a=".".join(["AAAA"*(len(x)//4)+"B"*(len(x)%4) if len(x)%2 == 0 else "x" for x in input().split(".")])
print(a if 'x' not in a else -1)