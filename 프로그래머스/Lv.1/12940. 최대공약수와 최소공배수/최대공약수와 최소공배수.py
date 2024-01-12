def solution(n, m):
    if n == m:
        return [n, n]
    a, b = n, m
    while b:
        a, b = b, a%b
    return [a, (n*m)//a]