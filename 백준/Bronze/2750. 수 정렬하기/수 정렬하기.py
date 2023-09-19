a=open(0)
next(a)
print(*sorted([int(i) for i in a]), sep="\n")