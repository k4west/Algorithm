def bfs(s):
    order[0] += s
    for i, c in enumerate(trees[s]):
        if i:
            order[1] += s
        if c != '.':
            bfs(c)
    order[2] += s


N = int(input())
trees = {}
for _ in range(N):
    p, l, r = input().split()
    trees[p] = [l, r]

order = ['']*3
bfs('A')

print('\n'.join(order))
