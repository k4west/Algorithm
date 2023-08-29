N, B = map(int, input().split())
s = []
while N > 0:
    n = N % B
    s.append(chr(n+[55, 48][n < 10]))
    N //= B
print(("".join(s))[::-1])