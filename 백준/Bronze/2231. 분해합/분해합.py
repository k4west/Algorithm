import sys
N = int(sys.stdin.readline())
s = max(N - 63, 1)
for n in range(s,N):
    t = n + sum(map(int, str(n)))
    if t == N:
        print(n)
        break
else:
    print(0)