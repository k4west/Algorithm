L = int(input())
N = int(input())
cake = [0 for _ in range(L+1)]
expected_i = real_i = real = M = 0
for i in range(N):
    t = 0
    p, k = map(int, input().split())
    if M < (e := k-p+1):
        M = e
        expected_i = i+1
    for j in range(p, k+1):
        if not cake[j]:
            cake[j] = i+1
            t += 1
    if real < t:
        real = t
        real_i = i+1
print(expected_i, real_i, sep='\n')
