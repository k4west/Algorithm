import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, p = map(int, input().split())
    print(n, p)
    print(n*(p-2)+2)