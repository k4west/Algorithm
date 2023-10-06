import sys
from itertools import permutations
def f():
    N = int(sys.stdin.readline())
    pm = list(map(int, sys.stdin.readline().split()))
    for i in range(-1,-N,-1):
        if pm[i-1] > pm[i]:
            for j in range(-1,-N,-1):
                if pm[j] < pm[i-1]:
                    pm[i-1], pm[j] = pm[j], pm[i-1]
                    pm = pm[:i] + sorted(pm[i:], reverse=True)
                    return " ".join(map(str, pm))
    else: return -1
print(f())