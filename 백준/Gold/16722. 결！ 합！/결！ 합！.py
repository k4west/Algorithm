def same(p, q, r):
    return p == q == r


def diff(p, q, r):
    return p+q+r == 7


def check(p, q, r):
    for x, y, z in zip(p, q, r):
        if not same(x, y, z) and not diff(x, y, z):
            return False
    return True


d = {"CIRCLE": 1, "TRIANGLE": 2, "SQUARE": 4, "YELLOW": 1, "RED": 2, "BLUE": 4, "GRAY": 1, "WHITE": 2, "BLACK": 4}
cards = tuple(tuple(map(lambda x: d[x], input().split())) for _ in range(9))
hap = set()
for i in range(7):
    a = cards[i]
    for j in range(i+1, 8):
        b = cards[j]
        for k in range(j+1, 9):
            c = cards[k]

            if check(a, b, c):
                hap.add((i+1, j+1, k+1))

score = 0
v = set()
g = True
for _ in range(int(input())):
    yell, *nums = input().split()
    if yell == 'H':
        a, b, c = map(int, nums)
        h = tuple(sorted([a, b, c]))
        if h in hap and h not in v:
            score += 1
            v.add(h)
        else:
            score -= 1
    else:
        if g and len(hap) == len(v):
            score += 3
            g = False
        else:
            score -= 1

print(score)
