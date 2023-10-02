import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
s = sys.stdin.readline()
i, c, t = 0, 0, 0
while i < M-2:
    if s[i:i+3] == 'IOI':
        t += 1
        i += 2
        if t == N:
            c += 1
            t -= 1
    else:
        i += 1
        t = 0
print(c)