import sys

input = lambda: int(sys.stdin.readline())
arr = [1, 2]
h = lambda k: 2 * (k**2) + 4 * k + 5
ans = []
for _ in range(input()):
    if (n := input()) < 2:
        ans.append(arr[n])
    else:
        k = n - 2
        ans.append(h(k))

print("\n".join(map(str, ans)))