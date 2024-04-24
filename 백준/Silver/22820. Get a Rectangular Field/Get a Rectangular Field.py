import sys

d = ((1, 0), (0, 1))
n, *list = sys.stdin.readlines()
ans = []
for i in range(int(n)):
    maps = [line.rstrip().split() for line in list[i * 6 : (i + 1) * 6]]
    m = 0
    for j in range(5):
        for k in range(5):
            for s in range(1, 6 - j):
                for t in range(1, 6 - k):
                    if all(
                        maps[p][q] == "1"
                        for p in range(j, j + s)
                        for q in range(k, k + t)
                    ):
                        if m < s * t:
                            m = s * t
    ans.append(m)
print(*ans, sep="\n")