def isPrime(n:int)->int:
    p = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i): p[j] = False
    return p

def isSquare(n:int)->int:
    if int(n**0.5) ** 2 == n: return n
    return 0

def P2(A: list) -> int:
    if (n := len(A)) < 2: return 0
    s = 0
    for p, a in zip(isPrime(n), A):
        if p and a > 0: s += isSquare(a)
    return s