import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    pattern = [list(input().strip()) for _ in range(N)]

    def row(i, j):
        for k in range(j, M):
            if pattern[i][k] != '-':
                break
            pattern[i][k] = False

    def col(i, j):
        for k in range(i, N):
            if pattern[k][j] != '|':
                break
            pattern[k][j] = False

    c = 0
    for i in range(N):
        for j in range(M):
            if not (p:=pattern[i][j]):
                continue
            if p == '-':
                c += 1
                row(i, j)
            elif p == '|':
                c += 1
                col(i, j)

    print(c)

if __name__ == "__main__":
    main()