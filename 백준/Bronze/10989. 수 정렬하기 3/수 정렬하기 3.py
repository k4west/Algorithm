import sys
N = int(sys.stdin.readline())
s = {}
for i in range(N):
    n = sys.stdin.readline().rstrip()
    if n in s:
        s[n] += 1
    else: 
        s[n] = 1
for n in range(1, 10001):
    n = str(n)
    if n in s:
        for _ in range(s[n]):
            print(n)