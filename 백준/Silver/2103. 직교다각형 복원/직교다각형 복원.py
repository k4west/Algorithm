import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    rows = [[] for _ in range(10001)]
    cols = [[] for _ in range(10001)]
    for _ in range(n):
        i, j = map(int, input().split())
        rows[i].append(j)
        cols[j].append(i)

    ans = 0
    for row in rows:
        row.sort()
        for i in range(0, len(row), 2):
            ans += row[i + 1] - row[i]
    for col in cols:
        col.sort()
        for i in range(0, len(col), 2):
            ans += col[i + 1] - col[i]
    print(ans)
main()