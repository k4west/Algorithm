import sys
n = int(sys.stdin.readline())
if n != 3 and n != 1:
    q, r = n//5, n%5
    if r%2:
        a = q + (r+5)//2 - 1
    else:
        a = q + r//2
    print(a)
else:
    print(-1)