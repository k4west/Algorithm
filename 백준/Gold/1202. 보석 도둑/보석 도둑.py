import sys
from heapq import heappush, heappushpop
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    gem, bag, q = [], [], []

    for _ in range(N): gem.append(tuple(map(int, input().split())))
    for _ in range(K): bag.append(int(input()))
    gem.sort()
    bag.sort()

    flag = False
    while gem:
        m, v = gem.pop()
        if bag and m <= bag[-1]:
            heappush(q, v)
            bag.pop()
            flag = True
        elif flag and v > q[0]: heappushpop(q, v)

    print(sum(q))

if __name__ == "__main__":
    main()