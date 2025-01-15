primes = [2, 3, 5, 7, 11]

def powmod(a, d, n):
    result = 1
    while d > 0:
        if d%2: result = (result*a)%n
        a = (a*a)%n
        d //= 2
    return result

def miller_rabin(n):
    s, d = 0, n-1
    while d%2 == 0:
        s += 1
        d //= 2
    for a in primes:
        if a == n: break
        x = powmod(a, d, n)
        if x == 1 or x == n-1: continue
        for _ in range(s-1):
            x = powmod(x, 2, n)
            if x == n-1: break
        else: return False
    return True
    
def main():
    cnt = 0
    for n in map(int, open(0).read().split()[1:]):
        cnt += miller_rabin(2*n+1)
    print(cnt)

if __name__ == "__main__":
    main()