import sys
def f():
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    A, B = a*d+b*c, b*d
    q, r = A, B
    while q%r:
        q, r = r, q%r
    print(A//r, B//r)
if __name__=="__main__":
    f()