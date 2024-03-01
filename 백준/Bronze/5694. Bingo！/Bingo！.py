import sys

def main():
    input = sys.stdin.readline
    while True:
        N, B = map(int, input().split())
        if N == 0:
            break
        cards = sorted(map(int, input().split()))
        tmp = set()
        for i in range(B - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                tmp.add(cards[i] - cards[j])
        print("YN"[bool(set(range(1, N + 1)) - tmp)])

main()