def make_prime(N):
    primes = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            for j in range(i**2, N + 1, i):
                primes[j] = False
    return primes


def main():
    import sys
    input = lambda: int(sys.stdin.readline())
    N, K = input(), input()
    nums = [False] + [True] * (N)
    primes = make_prime(N)

    for n in range(K + 1, N + 1):
        if primes[n] and K < n:
            for i in range(n, N + 1, n):
                nums[i] = False
    print(sum(nums))


if __name__ == "__main__":
    main()