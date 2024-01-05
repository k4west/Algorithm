import sys
input = sys.stdin.readline
N, M = map(int, input().split())
order = set(input().split()[:M])
friends = set(input().split())
print(len(order-friends))