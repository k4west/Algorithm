import sys
input = sys.stdin.readline


N, R = map(int, input().split())
N2 = 1 << N
A = [[*map(int, input().split())] for _ in range(N2)]

for _ in range(R):
    k, l = map(int, input().split())
    l2 = 1 << l
    tmp = [row[:] for row in A]
    if k == 1:
        # if not l:
        #     continue
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[r+l2-1-dr][c+dc]
    elif k == 2:
        # if not l:
        #     continue
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[r+dr][c+l2-1-dc]
    elif k == 3:
        # if not l:
        #     continue
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[r+l2-1-dc][c+dr]
    elif k == 4:
        # if not l:
        #     continue
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[r+dc][c+l2-1-dr]
    elif k == 5:
        m = N2-l2
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[m-r+dr][c+dc]
    elif k == 6:
        m = N2-l2
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[r+dr][m-c+dc]
    elif k == 7:
        m = N2-l2
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[m-c+dr][r+dc]
    elif k == 8:
        m = N2-l2
        for r in range(0, N2, l2):
            for c in range(0, N2, l2):
                for dr in range(l2):
                    for dc in range(l2):
                        A[r+dr][c+dc] = tmp[c+dr][m-r+dc]
    
    # print(k, l, l2)
    # print("\n".join(" ".join(map(lambda x: str(x).rjust(2), row)) for row in A))
    # print("=======")

print("\n".join(" ".join(map(str, row)) for row in A))
