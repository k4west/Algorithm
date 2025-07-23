P = int(input())
ans = []
for _ in range(P):
    count = 0
    T, *heights = map(int, input().split())
    for i, h in enumerate(heights):
        for p in heights[:i]:
            if p > h:
                count += 1
    ans.append(' '.join(map(str, (T, count))))
print('\n'.join(ans))
