import sys
_ = sys.stdin.readline()
d = {}
for i in sys.stdin.readline().split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
n = sys.stdin.readline().rstrip()
print(d[n] if n in d else 0)