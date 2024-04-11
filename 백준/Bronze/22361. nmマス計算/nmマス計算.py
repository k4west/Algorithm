import sys

input = sys.stdin.readline
ans = []

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    a = map(int, input().split())
    b = list(map(int, input().split()))
    c = [0] * 10
    for i in a:
        for j in b:
            for k in map(int, str(i * j)):
                c[k] += 1
    ans.append(" ".join(map(str, c)))

print("\n".join(ans))