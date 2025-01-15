primes = [2, 7, 61]

def powmod(a, d, n):
    result = 1
    while d > 0:
        if d%2: result = (result*a)%n
        a = (a*a)%n
        d //= 2
    return result

def miller_rabin(m):
    s, d = 0, m-1
    while d%2 == 0:
        s += 1
        d //= 2
    for a in primes:
        x = powmod(a, d, m)
        if x == 1 or x == m-1: continue
        for _ in range(s-1):
            x = powmod(x, 2, m)
            if x == m-1: break
        else: return False
    return True
    
def main():
    cnt = 0
    for n in map(int, open(0).read().split()[1:]):
        cnt += miller_rabin((m:=2*n+1)) or m in primes
    print(cnt)

if __name__ == "__main__":
    main()