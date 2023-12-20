def main():
    N = int(input())

    nums = [False, False] + [True]*(N-1)
    for i in range(2, int(N**.5)+1):
        if nums[i]:
            for j in range(i*i, N+1, i):
                nums[j] = False

    primes = [n for n in range(1, N+1) if nums[n]]
    if not primes:
        print(0)
        return
    E = len(primes)
    s, e, tmp, c = 0, 1, 2, 0
    while s < e:
        while tmp < N and e < E:
            tmp += primes[e]
            e += 1
        if tmp == N:
            c += 1
            
        tmp -= primes[s]
        s += 1
    print(c)  

if __name__ == "__main__":
    main()