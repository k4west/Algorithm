import sys
n = int(sys.stdin.readline())
d = dict()
for _ in range(n):
    i = sys.stdin.readline().split()
    if i[0] == "1":
        d[i[2]] = i[1]
    else:
        print(d[i[1]])