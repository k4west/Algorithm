from sys import stdin
from itertools import permutations


input = stdin.readline


def rotate(arr):
    return [list(col[::-1]) for col in zip(*arr)]


def rotated_ing(arr):
    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    return arr, arr1, arr2, arr3


def apply_ing(pot, ing):
    q, c, s = pot
    q, c = q[:], c[:]
    ps, qs, cs = ing

    for t in range(16):
        pi, cq, cc = ps[t], qs[t], cs[t]
        pq = q[pi]
        pc = c[pi]

        if pc:
            s -= pq * pc

        nq = pq + cq
        if nq < 0:
            nq = 0
        elif nq > 9:
            nq = 9
        q[pi] = nq

        if cc:
            c[pi] = cc
            s += nq * cc
        elif pc:
            s += nq * pc
    return q, c, s


ans = 0
color_weight = {k: v for k, v in zip("WRBGY", (0, 7, 5, 3, 2))}
index_li = [tuple(5*i+j+off for i in range(4) for j in range(4)) for off in (0, 1, 5, 6)]

ingredients = []
for _ in range(int(input())):
    quality = [[*map(int, input().split())] for _ in range(4)]
    color = [[color_weight[c] for c in input().split()] for _ in range(4)]
    qualities = rotated_ing(quality)
    colors = rotated_ing(color)

    ingredient = []
    for k in range(4):
        qk = tuple(qualities[k][i][j] for i in range(4) for j in range(4))
        ck = tuple(colors[k][i][j] for i in range(4) for j in range(4))
        for index in index_li:
            ingredient.append((index, qk, ck))
    ingredients.append(ingredient)


pot_q = [0] * 25
pot_c = [0] * 25
for ing0, ing1, ing2 in permutations(ingredients, 3):   # 재료 3개 선정 (720)
    for p0 in range(16):
        pot_state1 = apply_ing((pot_q, pot_c, 0), ing0[p0])
        for p1 in range(16):
            pot_state2 = apply_ing(pot_state1, ing1[p1])
            for p2 in range(16):
                _, _, score = apply_ing(pot_state2, ing2[p2])

                if ans < score:
                    ans = score
print(ans)