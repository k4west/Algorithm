def main():
    primes = [2, 7, 61]
    cnt = 0
    for n in map(int, open(0).read().split()[1:]):
        if (m:=2*n+1) in primes or n < 4:
            cnt += 1
            continue
        flag = True
        s, d = 0, m-1
        while d%2 == 0:
            s += 1
            d //= 2
        for a in primes:
            x = pow(a, d, m)
            if x == 1 or x == m-1: continue
            for _ in range(s-1):
                x = pow(x, 2, m)
                if x == m-1: break
            else:
                flag = False
                break
        cnt += flag
    print(cnt)
main()