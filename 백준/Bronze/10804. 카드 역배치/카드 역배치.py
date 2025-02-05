*cards, = map(str, range(21))
for i in open(0):
    a, b = map(int, i.split())
    cards[a:b+1] = cards[b:a-1:-1]
print(" ".join(cards[1:]))