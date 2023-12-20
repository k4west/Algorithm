def main():
    import sys
    N = int(sys.stdin.readline())

    nums = [False, False] + [True]*(N-1)
    for i in range(2, int(N**.5)+1):
        if nums[i]:
            for j in range(i*i, N+1, i):
                nums[j] = False

    primes = [n for n in range(1, N+1) if nums[n]]
    if not primes:
        print(0)
        return
    tmp = c = 0
    _p = iter(primes)
    for p in primes:
        tmp += p
        while tmp > N:
            tmp -= next(_p)
        if tmp == N:
            c += 1
    print(c)  

if __name__ == "__main__":
    main()