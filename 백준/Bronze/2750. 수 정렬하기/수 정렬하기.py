a=open(0)
next(a)
li = sorted([int(i) for i in a])
print(*li, sep="\n")