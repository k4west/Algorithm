import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    n = int(input())
    s = sum(int(input()) for _ in range(n))
    if s%n: print("NO")
    else: print("YES")