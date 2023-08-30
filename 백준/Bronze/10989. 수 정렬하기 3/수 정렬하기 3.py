import sys
N = int(sys.stdin.readline())
s = [0]*10001
for _ in range(N):
    n = int(sys.stdin.readline())
    s[n] += 1
for n in range(1, 10001):
    if s[n]:
        for _ in range(s[n]):
            sys.stdout.write(str(n)+"\n")
    elif not sum(s[n:]):
        break