import sys
s = sys.stdin.readline().strip()
print(*sorted([s[a:] for a in range(len(s))]), sep="\n")