import sys
n = int(sys.stdin.readline())

if n != 3 and n != 1:
    q, r = n//5, n%5 
    print(q + (r+5*(r%2))//2 - r%2)
else:
    print(-1)