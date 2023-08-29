import sys
N, B = sys.stdin.readline().split()
B, s = int(B), 0
for i, n in enumerate(N[::-1]):
    if n.isdigit():
        s += int(n) * (B**i)
    else:
        s += (ord(n)-55) * (B**i)
print(s)