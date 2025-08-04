ans = []
T = int(input())
for _ in range(T):
    N = int(input())
    roots = [0]*(N+1)

    for _ in range(N-1):
        p, c = map(int, input().split())
        roots[c] = p

    s, e = map(int, input().split())
    li = [0]*(N+1)
    li[s] = 1
    while roots[s]:
        s = roots[s]
        li[s] = 1

    while not li[e]:
        e = roots[e]

    ans.append(e)

print('\n'.join(map(str, ans)))
