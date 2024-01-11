import sys

input = lambda: int(sys.stdin.readline())
N, K = input(), input()
nums = [False] + [True] * (N)
c = K if N >= K else N
primes = [False, False] + [True] * (N - 1)

for i in range(2, int(N**.5) + 1):
    if primes[i]:
        for j in range(i**2, N + 1, i):
            primes[j] = False
primes = [i for i, b in enumerate(primes[2 : K + 1], 2) if b]

for n in range(K + 1, N + 1):
    if nums[n]:
        flag = False
        for p in primes:
            while not n % p:
                n //= p
            if n <= K or n == 1:
                c += 1
                flag = True
                break
                
print(c)