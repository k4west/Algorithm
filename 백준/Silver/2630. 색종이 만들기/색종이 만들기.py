def f(r, c, n):
    if not n:
        return
    
    s = sum(sum(row[c:c+n]) for row in paper[r:r+n])
    if s == n*n:
        ans[1] += 1
    elif not s:
        ans[0] += 1
    else:
        n //= 2
        f(r, c, n)
        f(r, c+n, n)
        f(r+n, c, n)
        f(r+n, c+n, n)


ans = [0, 0]
N = int(input())
paper = [[*map(int, input().split())] for _ in range(N)]
f(0, 0, N)
print(*ans, sep='\n')