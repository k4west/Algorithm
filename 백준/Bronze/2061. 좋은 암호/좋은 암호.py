import sys

ans = "GOOD"
K, L = map(int, sys.stdin.readline().split())
for i in range(2, L):
    if not K % i:
        ans = f"BAD {i}"
        break
print(ans)