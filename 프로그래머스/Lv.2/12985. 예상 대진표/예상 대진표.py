def solution(n,a,b):
    i = 1
    if not a % 2:
        a -= 1
    if not b % 2:
        b -= 1
    while True:
        a, b = a >> 1, b >> 1
        if a == b:
            return i
        i += 1