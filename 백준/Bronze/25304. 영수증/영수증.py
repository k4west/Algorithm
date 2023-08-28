import sys
c = int(sys.stdin.readline())
N = int(sys.stdin.readline())
s = 0
for _ in range(N):
    t = eval("*".join(sys.stdin.readline().split()))
    s += t
if c == s:
    print("Yes")
else:
    print("No")