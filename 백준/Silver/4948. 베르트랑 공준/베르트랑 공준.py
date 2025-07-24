nums = []
M = 0
while num := int(input()):
    nums.append(num)
    if M < num:
        M = num

primes = [0, 0, 1] + [1, 0] * (M-1)
for i in range(3, int((2*M)**.5)+1):
    if primes[i]:
        for j in range(i*i, 2*M+1, i):
            primes[j] = 0

for i in range(1, 2*M+1):
    primes[i] += primes[i-1]

print(*[primes[2*n] - primes[n] for n in nums], sep='\n')
