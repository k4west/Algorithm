def check(i, j):
    return (i == 0 and 0 <= j < 10) or (i == 1 and 0 <= j < 9) or (i == 2 and 0 <= j < 7)


def bfs(string):
    move = 0
    sr, sc = keyboard[string[0]]

    for e in string[1:]:
        er, ec = keyboard[e]
        if sr == er and sc == ec:
            continue

        q, nq = [(sr, sc)], []
        visited = {(sr, sc)}

        while q or nq:
            if not q:
                q, nq = nq, []
                move += 1

            r, c = q.pop()
            for dr, dc in d:
                nr = r + dr
                nc = c + dc

                if nr == er and nc == ec:
                    move += 1
                    q = nq = []
                    break

                if check(nr, nc) and not (nr, nc) in visited:
                    visited.add((nr, nc))
                    nq.append((nr, nc))

        sr, sc = er, ec

    return 2*move + len(string)


ans = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1))
keyboard = {}
for i, row in enumerate(["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]):
    for j, k in enumerate(row):
        keyboard[k] = (i, j)

print("\n".join(map(str, [bfs(input()) for _ in range(int(input()))])))