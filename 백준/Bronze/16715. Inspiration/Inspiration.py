import sys

N = int(sys.stdin.readline())
m, no = 0, 2
for i in range(2, N + 1):
    tmp = []
    n, s = N, 0
    while n:
        s += n % i
        n = n // i
    if m < s:
        m, no = s, i
print(m, no)