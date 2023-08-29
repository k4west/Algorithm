import sys
s = set([int(i) for i in sys.stdin.readlines()[1:]])
li = sorted(list(s))
print(*li, sep="\n")