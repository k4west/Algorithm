def check(r, c):
    return 0 > r or r >= R or a[r][c]!='.'

def dfs(r, c):
    if check(r, c):
        return False
    a[r][c] = 'x'
    if c == C-1:
        return True
    for dr in d:
        if dfs((nr:=r+dr), c+1):
            return True
    return False

if __name__ == '__main__':
    d = (-1, 0, 1)
    a = open(0)
    R, C = map(int, next(a).split())
    a = [*map(list, a.read().split())]
    print(sum(dfs(r, 1) for r in range(R)))