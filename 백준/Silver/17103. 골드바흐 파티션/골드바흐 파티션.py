T, *nums, = map(int, open(0))
M = max(nums)
primes = [0, 0, 1] + [1, 0] * (M//2-1)
for i in range(3, int(M**.5)+1):
    if primes[i]:
        for j in range(i*i, M+1, i):
            primes[j] = 0
print(*[sum(1 for i in range(n//2+1) if primes[i] & primes[n-i]) for n in nums], sep="\n")
