import sys
input = sys.stdin.readline

T = int(input())
c = [0] * T

for t in range(T):
    N, M = map(int, input().split())
    L = list(map(int,input().split()))
    l = [0] * len(L)
    l[M] = 1
    while True:
        if L[0] < max(L):
            L.append(L.pop(0))
            l.append(l.pop(0))
        else:
            L.pop(0)
            l.pop(0)
            c[t] += 1
            if not 1 in l:
                break 
print(*c, sep = "\n")