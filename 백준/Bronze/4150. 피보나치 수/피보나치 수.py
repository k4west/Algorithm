def mul(A: list, B: list) -> list:
    return [
        A[0] * B[0] + A[1] * B[1],
        A[0] * B[1] + A[1] * B[2],
        A[1] * B[1] + A[2] * B[2],
    ]


def sol(n, A):
    if n == 1:
        return A
    elif n % 2:
        return mul(mul(sol(n // 2, A), sol(n // 2, A)), [1, 1, 0])
    else:
        return mul(sol(n // 2, A), sol(n // 2, A))


print(sol(int(input()), [1, 1, 0])[1])