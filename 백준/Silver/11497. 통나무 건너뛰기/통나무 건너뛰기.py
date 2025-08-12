ans = []
for _ in range(int(input())):
    N = int(input())
    *L, = map(int, input().split())
    L.sort()

    level = max(L[1] - L[0], L[-1] - L[-2])
    for i in range(2, N):
        t = L[i] - L[i-2]
        if level < t:
            level = t

    ans.append(level)
print("\n".join(map(str, ans)))
