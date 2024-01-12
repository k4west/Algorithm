def solution(n):
    tri = []
    while n:
        tri.append(n%3)
        n //= 3
    ans = 0
    for i, t in enumerate(tri[::-1]):
        ans += t*(3**i)
    return ans