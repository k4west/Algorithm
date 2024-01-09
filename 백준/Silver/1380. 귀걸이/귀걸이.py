import sys

input = sys.stdin.readline
ans, sn = [], 1
while True:
    n = int(input())
    if not n:
        break
    students = [input().rstrip() for _ in range(n)]
    check = 0
    for _ in range(2 * n - 1):
        check ^= int(input().split()[0])
    ans.append(" ".join((str(sn), students[check - 1])))
    sn += 1
print("\n".join(ans))