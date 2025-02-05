def main():
    cards = [i for i in range(21)]
    for i in open(0):
        a, b = map(int, i.split())
        cards[a:b+1] = cards[b:a-1:-1]
    print(" ".join(map(str, cards[1:])))

main()