import sys
input = sys.stdin.readline
N, B = map(int, input().split())
while N != 0:
    cards = sorted(map(int, input().split()))
    tmp = set(cards[i] - cards[j] for i in range(B - 1, -1, -1) for j in range(i - 1, -1, -1))
    if set(range(1, N + 1)) - tmp: print("N")
    else: print("Y")
    N, B = map(int, input().split())