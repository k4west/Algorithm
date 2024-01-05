import sys

input = sys.stdin.readline
N, M = map(int, input().split())
order = list(map(int, input().split()))
friends = set(map(int, input().split()))
l, v, c = len(friends), set(), 0

for i in range(N):
    if l == len(v):
        break
    for j in range(N - 1, i, -1):
        if (s := order[i]) in friends:
            v.add(s)
            break
        if (t := order[j]) not in friends:
            continue
        order[j], order[i] = s, t
        v.add(t)
        c += 1
        break
print(c)