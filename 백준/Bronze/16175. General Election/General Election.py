import sys

input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    N, M = map(int, input().split())
    votes = [0] * N
    for _ in range(M):
        for i, v in enumerate(map(int, input().split())):
            votes[i] += v
    m, idx = 0, 0
    for i, v in enumerate(votes, 1):
        if m < v:
            m = v
            idx = i

    ans.append(idx)
print("\n".join(map(str, ans)))