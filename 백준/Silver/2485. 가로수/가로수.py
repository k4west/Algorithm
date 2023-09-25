import sys
def g(q, r):
    while q%r: q, r = r, q%r
    return r
def f():
    n = int(sys.stdin.readline())
    li = []
    for _ in range(n): li.append(int(sys.stdin.readline()))
    a = [li[i] - li[i-1] for i in range(1, n)]
    r = a[0]
    for i in range(1, len(a)): r = g(r, a[i])        
    print(sum([i//r - 1 for i in a]))
if __name__=="__main__":
    f()