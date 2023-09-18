N = int(input())
t = []
for n in range(2, int(N**.5)+1):
    c = 0
    while not N%n:
        print(n)
        N //= n
if N!=1: print(N)