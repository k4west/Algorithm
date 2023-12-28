import sys
input = sys.stdin.readline

N, T, P = map(int, input().split())
if not N:
    print(1)
else:
    rank = []
    scores = sorted(list(map(int, input().split())) + [T], reverse=True)
    if N == P and scores[-1] == T:
        print(-1)
    else:
        print(scores.index(T)+1)