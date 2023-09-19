import sys
def f(X):
    d = {x:i for i, x in enumerate(sorted(set(X)))}
    li = [d[x] for x in X]
    print(*li)
sys.stdin.readline()
X = list(map(int, sys.stdin.readline().split()))
f(X)