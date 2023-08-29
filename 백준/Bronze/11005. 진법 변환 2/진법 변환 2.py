import sys
N, B = map(int, sys.stdin.readline().split())
s = []
while N > 0:
    n = N % B
    if n < 10:
        s.append(str(n))
    else:
        s.append(chr(n+55))
    N //= B
print("".join(s[::-1]))