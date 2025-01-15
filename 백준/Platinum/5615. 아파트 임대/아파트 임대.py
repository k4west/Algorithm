def main():
    primes = [2, 3, 5, 7, 11]
    cnt = 0
    for n in map(int, open(0).read().split()[1:]):
        flag = True
        m = 2*n+1
        s, d = 0, m-1
        while d%2 == 0:
            s += 1
            d //= 2
        for a in primes:
            x, y = 1, d
            while y > 0:
                if y%2: x = (x*a)%m
                a = (a*a)%m
                y //= 2
            if x == 1 or x == m-1: continue
            for _ in range(s-1):
                x = x*x%m
                if x == m-1: break
            else:
                flag = False
                break
        cnt += flag or m in primes
    print(cnt)
main()