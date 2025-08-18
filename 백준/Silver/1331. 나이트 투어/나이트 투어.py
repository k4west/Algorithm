def check(a, b):
    return {abs(a[0] - b[0]), abs(a[1] - b[1])} == {1, 2}


ans = "Invalid"
d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}  # 상하좌우
p = {a: i for a, i in zip("ABCDEF123456", [*range(1, 7)]*2)}

N = 6   # 6×6 체스판
chess = [list('.'*N) for _ in range(N)]
trace = [tuple(map(lambda x: p[x], input())) for _ in range(36)]

if len(set(trace)) == 36:
    for i in range(36):
        if not check(trace[i-1], trace[i]):
            break
    else:
        ans = "Valid"
print(ans)
