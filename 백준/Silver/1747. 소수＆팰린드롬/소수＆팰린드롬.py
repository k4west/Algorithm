def f(s):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]: return False
    return True

def g(n,m=1003001):
    primes = [False, False] + [True]*(m-1)
    for i in range(2, m+1):
        if primes[i]:
            if i >= n and f(str(i)):print(i); return
            for j in range(i*i, m, i):primes[j] = False

if __name__ == '__main__':
    n=int(input())
    if n==1:print(2)
    else: g(n)