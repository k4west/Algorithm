cards = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    cards[a:b+1] = cards[b:a-1:-1]
print(*cards[1:])