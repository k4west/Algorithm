import sys

N = int(sys.stdin.readline())
m, no = 0, 2
for i in range(2, N + 1):
    tmp = []
    n, s, j = N, 0, 0
    while n >= i ** (j + 1):
        j += 1
    while n:
        t, n = n // (i**j), n % (i**j)
        s += t
        j -= 1
        if m < s:
            m, no = s, i
print(m, no)