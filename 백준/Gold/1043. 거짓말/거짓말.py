import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n, *k = map(int, input().split())
meeting = [{*list(map(int, input().split()))[1:]} for _ in range(M)]
if not n:
    print(M)
else:
    k, c = {*k}, 0
    for _ in range(M):
        for m in meeting:
            if k&m:
                k |= m
    for m in meeting:
        if not k&m:
            c += 1
    print(c)