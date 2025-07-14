def mul(li):
    m = 1
    for i in li:
        m *= i
    return m

N = int(input())
*trees, = map(int, input().split())
M = 0
for i in range(N-3):
    for j in range(i+1, N-2):
        for k in range(j+1, N-1):
            t = mul(trees[:i+1]) + mul(trees[i+1:j+1]) + mul(trees[j+1:k+1]) + mul(trees[k+1:])
            if t > M:
                M = t
print(M)