N = int(input())
cards = list(map(int, input().split()))
ans = [-1]*1000001
for i in cards: ans[i] = 0
_sorted = sorted(cards)
M = _sorted[-1]

for i in range(N-1):
    p = _sorted[i]
    for j in range(2, M//_sorted[i]+1):
        if ans[p*j] != -1:
            ans[p*j] += 1
            ans[p] -= 1
print(*(-ans[cards[i]] for i in range(N)))