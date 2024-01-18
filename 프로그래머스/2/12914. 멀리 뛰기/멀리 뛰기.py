def solution(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, (a+b)%1234567
    return b