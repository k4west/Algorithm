def f(n,p):
    a, b = 1,1
    for _ in range(n//2-1):
        a, b = b, (a+b)%p
    if n % 2:
        return (pow(b,2)+pow(a,2)) % p
    else:
        return (pow(b,2)-pow(b-a,2)) % p
n = int(input()) + 1
print(f(n, 15746))