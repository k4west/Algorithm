import sys
input = sys.stdin.readline
N, B = map(int, input().split())
while N != 0:
    tmp = set()
    cards = sorted(map(int, input().split()))
    for i in range(B - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            tmp.add(cards[i] - cards[j])
    if set(range(1, N + 1)) - tmp: print("N")
    else: print("Y")
    N, B = map(int, input().split())

