import sys
input = sys.stdin.readline
ans = []
M = 10**6
for i in range(int(input())):
    p = [min(a, b, c) for a, b, c in zip(map(int, input().split()), map(int, input().split()), map(int, input().split()))]
    if (s:=sum(p)) < M:
        ans.append(f"Case #{i+1}: IMPOSSIBLE")
    else:
        d = s - M
        j = 0
        while d:
            t = min(d, p[j])
            p[j] -= t
            d -= t
            j += 1
        ans.append(f"Case #{i+1}: " + " ".join(map(str, p)))
print("\n".join(ans))