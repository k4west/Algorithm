def get_primes(N):
    nums = [True]*(N+1)
    for i in range(3, int(N**.5)+1, 2):
        if nums[i]:
            nums[i*i :: 2*i] = [False]*((N-i*i)//(2*i)+1)
    return [2] + [n for n in range(3, N+1, 2) if nums[n]]

def main():
    import sys
    N = int(sys.stdin.readline())

    primes = get_primes(N)
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