import sys
input = sys.stdin.readline
ans = []
def gcd(x, y):
    while x % y: x, y = y, x % y
    return y
def finite_decimal_number(z, b):
    prime_factors_of_b = []
    for p in range(2, b + 1):
        if b % p == 0:
            prime_factors_of_b.append(p)
            while b % p == 0: b //= p
    for p in prime_factors_of_b:
        while z % p == 0: z //= p
    return z == 1
def cal_period(x, y, b):
    d, idx = {x: 0}, 1
    current = x * b
    while True:
        current %= y
        if current in d: return idx - d[current]
        d[current] = idx
        idx += 1
        current *= b
for i in range(int(input())):
    b, x, y = input().rstrip().split()
    b = int(b)
    x, y = int(x, b), int(y, b)
    d = gcd(x, y)
    x //= d
    y //= d
    if finite_decimal_number(y, b): period = 0
    else: period = cal_period(x, y, b)
    ans.append(f"Scenario #{i+1}:\n{period}")
print("\n\n".join(ans))
