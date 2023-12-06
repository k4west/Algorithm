N = int(input())
cards = list(map(int, input().split()))
M = max(cards)+1
v = [False]*M
ans = [0]*M
for card in cards:
    v[card] = True
for card in cards:
    for i in range(2*card, M, card):
        if v[i]:
            ans[card] += 1
            ans[i] -= 1
print(*(ans[card] for card in cards))