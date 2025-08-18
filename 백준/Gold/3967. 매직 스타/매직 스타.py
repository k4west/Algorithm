hexagram = [
    [(1, 1), (1, 3), (1, 5), (1, 7)],
    [(3, 1), (3, 3), (3, 5), (3, 7)],
    [(0, 4), (1, 3), (2, 2), (3, 1)],
    [(0, 4), (1, 5), (2, 6), (3, 7)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
    [(1, 7), (2, 6), (3, 5), (4, 4)]
]


def check_sum():
    for i, pos in enumerate(hexagram):
        if sum(alpha2num(star[r][c]) for r, c in pos) != 26:
            return
    print("\n".join("".join(row) for row in star))
    exit()


def alpha2num(a):
    return (ord(a)-64) % 56


def num2alpha(n):
    return chr(n+64)


def bt(n):
    if n == N:
        return check_sum()

    for i in range(N):
        if not v[i]:
            v[i] = 1
            star[unfilled[n][0]][unfilled[n][1]] = alphas[i]
            bt(n+1)
            v[i] = 0


star = [list(input()) for _ in range(5)]
alphas = sorted(set(map(num2alpha, range(1, 13))) - {star[r][c] for r, c in sum(hexagram, []) if star[r][c] != 'x'})
unfilled = sorted(set(sum([[(r, c) for r, c in pos if star[r][c] == 'x'] for pos in hexagram], [])))
state = []

N = len(alphas)
v = [0]*N

bt(0)
