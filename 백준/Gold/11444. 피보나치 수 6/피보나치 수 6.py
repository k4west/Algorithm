def f(n, p):
    if n == 1:
        return [[1, 1], [1, 0]]
    M = f(n//2, p)
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    M[0][0] = (pow(a, 2, p) + b*c%p) % p
    M[0][1] = b*((a+d)%p)%p
    M[1][0] = c*((a+d)%p)%p
    M[1][1] = (pow(d, 2, p) + b*c%p) % p
    if n%2: 
        return [[(M[0][0] + M[0][1]) % p, M[0][0]], [(M[1][0] + M[1][1]) % p, M[1][0]]]
    else:
        return M

n = int(input())
print(f(n, 1_000_000_007)[0][1])