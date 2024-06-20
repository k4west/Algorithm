def g(m=1003001):
    primes = [False, False, True] + [True, False]*(m//2)
    for i in range(3, int(m**.5)+1):
        if primes[i]:
            for j in range(i*i, m, i):
                primes[j] = False
    return primes

def f(s):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]: return False
    return True

n=int(input())
primes = g()
while True:
    if primes[n] and f(str(n)):
        print(n)
        break 
    n+=1