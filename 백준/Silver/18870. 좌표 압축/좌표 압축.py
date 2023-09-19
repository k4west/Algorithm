import sys
def f(X):
    d = {x:str(i) for i, x in enumerate(sorted(set(X)))}
    print(" ".join([d[x] for x in X]))
sys.stdin.readline()
X = list(map(int, sys.stdin.readline().split()))
f(X)