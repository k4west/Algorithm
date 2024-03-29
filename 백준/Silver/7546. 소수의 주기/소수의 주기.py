import sys

input = sys.stdin.readline
ans = []


# 분수를 약분하려고 최대공약수 구하는 함수
def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


# 유한 소수 판별 함수
def finite_decimal_number(z, b):
    # b의 약수 구하기
    prime_factors_of_b = []
    for p in range(2, b + 1):
        if b % p == 0:
            prime_factors_of_b.append(p)
            while b % p == 0:
                b //= p

    # 분모가 b의 약수의 곱으로만 이루어졌는지 확인
    for p in prime_factors_of_b:
        while z % p == 0:
            z //= p
    return z == 1


# 주기 계산 함수
def cal_period(x, y, b):
    d, idx = [0] * y, 1
    current = x * b
    while True:
        current %= y
        if d[current]:
            return idx - d[current]
        d[current] = idx
        idx += 1
        current *= b


for i in range(int(input())):
    b, x, y = input().rstrip().split()
    b = int(b)
    x, y = int(x, b), int(y, b)  # b진법으로 변환

    # 기약분수 만들기
    d = gcd(x, y)
    x //= d
    y //= d

    if finite_decimal_number(y, b):
        period = 0
    else:
        period = cal_period(x, y, b)

    ans.append(f"Scenario #{i+1}:\n{period}")
print("\n\n".join(ans))
