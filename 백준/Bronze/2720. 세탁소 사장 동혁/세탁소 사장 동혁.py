import sys
T = int(sys.stdin.readline())
for _ in range(T):
    i = int(sys.stdin.readline())
    for c in [25, 10, 5, 1]:
        print(i//c, end=" ")
        i %= c
    print()