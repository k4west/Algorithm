import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
ans = [2]*(a+b+c+1)
test_0 = []
for _ in range(int(input())):
    *parts, r = map(int, input().split())
    if r:
        for part in parts:
            ans[part] = 1
    else:
        test_0.append(parts)
for parts in test_0:
    for i in range(3):
        if ans[parts[i - 1]] * ans[parts[(i+1) % 3]] == 1:
            ans[parts[i]] = 0

print(*ans[1:], sep="\n")