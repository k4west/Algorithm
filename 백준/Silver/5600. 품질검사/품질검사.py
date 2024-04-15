a, b, c, n, *test = map(int, open(0).read().split())
ans = [2]*(a+b+c+1)
test_0 = []
for s in range(n):
    i, j, k, r = test[s*4:s*4+4]
    if r:
        ans[i] = ans[j] = ans[k] = 1
    else:
        test_0.append((i, j, k))
for parts in test_0:
    for s in range(3):
        if ans[parts[s-1]] * ans[parts[(s+1)%3]] == 1:
            ans[parts[s]] = 0

print(*ans[1:], sep="\n")