import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    gem, bag, q, i, ans = [], [], [], 0, 0

    for _ in range(N): gem.append(tuple(map(int, input().split())))
    for _ in range(K): bag.append(int(input()))
    gem.sort()
    bag.sort()

    for w in bag:
        while i < N and gem[i][0] <= w:
            heappush(q, -gem[i][1])
            i += 1
        if q: ans -= heappop(q)

    print(ans)

if __name__ == "__main__":
    main()
