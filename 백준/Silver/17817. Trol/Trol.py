import sys

input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    s = (diff := r - l + 1) // 9 * 45
    for i in range(diff % 9):
        s += (l + i) % 9 or 9
    ans.append(s)
print(*ans, sep="\n")