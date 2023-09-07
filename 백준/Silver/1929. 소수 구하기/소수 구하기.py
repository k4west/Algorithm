import sys

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    print(n)

M, N = map(int, sys.stdin.readline().split())
for n in range([M+1-M%2,2][M==2], N+1):
    if n == 1:
        continue
    isprime(n)