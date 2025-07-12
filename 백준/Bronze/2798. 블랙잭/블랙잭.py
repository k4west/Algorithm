N, M = map(int, input().split())
cards = sorted(map(int, input().split()))
A = m = 0
for i in range(N-2-m):
    a = cards[i]
    if a > M:
        break
    for j in range(i+1, N-1-m):
        b = cards[j]
        if a+b > M:
            break
        for k in range(j+1, N-m):
            c = cards[k]
            if (t:=a+b+c) > M:
                break
            if A < t:
                A = t
print(A)