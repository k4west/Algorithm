import sys
def f(n):
    a, b = 1, 1
    for _ in range(n//2-1):
        a, b = b, (a+b)
    if n % 2:
        return (pow(b,2)+pow(a,2))
    else:
        return (pow(b,2)-pow(b-a,2))

n = int(sys.stdin.readline())
if n in (0, 1): print(n)
else: print(f(n))