import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    tmp = []
    i = int(input())
    for c in (25, 10, 5, 1):
        tmp.append(i//c)
        i %= c
    print(" ".join(map(str, tmp)))