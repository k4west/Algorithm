import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    input()
    n = int(input())
    s = sum(int(input()) for _ in range(n))
    if s%n: ans.append("NO")
    else: ans.append("YES")
print("\n".join(ans))