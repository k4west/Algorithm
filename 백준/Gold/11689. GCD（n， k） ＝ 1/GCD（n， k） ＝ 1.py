import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def powmod(a, d, n):
    result = 1
    while d > 0:
        if d%2:
            result = (result*a)%n
        a = (a*a)%n
        d //= 2
    return result

def miller_rabin(n):
    s, d = 0, n-1
    while d%2 == 0:
        s += 1
        d //= 2
    for a in primes:
        if a >= n:
            break
        x = powmod(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = powmod(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def pollard_rho(n):
    g = lambda x, c: (((x*x)%n)+c)%n
    while True:
        x = y = 2
        c, d = random.randint(1, n-1), 1
        while d == 1:
            x = g(x, c)
            y = g(g(y, c), c)
            d = gcd(abs(x-y), n)
        if d != n:
            return d

def factorize(n):
    factors = []
    for p in primes:
        if n%p == 0:
            factors.append(p)
            while n%p == 0:
                n //= p
    def f(n):
        if n == 1:
            return
        if miller_rabin(n):
            factors.append(n)
            return
        d = pollard_rho(n)
        f(d)
        while n%d == 0:
            n //= d
        f(n)
    f(n)
    return factors
    
def main():
    n = int(open(0).read())
    if n < 3:
        print(1)
        return
    phi = n
    for p in set(factorize(n)):
        phi = phi // p * (p-1)
    print(phi)
main()