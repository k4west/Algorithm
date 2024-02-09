isPrime = [False, False] + [True]*9999998
for i in range(2, 3163):
    if isPrime[i]:
        for j in range(i*i, 9999998, i):
            isPrime[j] = False

from itertools import permutations
def solution(numbers):
    n = len(numbers)
    nums = set()
    for i in range(1, n+1):
        for perm in permutations(range(n), i):
            nums.add(int("".join(numbers[idx] for idx in perm)))
    return sum(isPrime[num] for num in nums)