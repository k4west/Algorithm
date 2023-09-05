import sys

def g(n):
    while n:
        if n%10 not in (5,8):
            return False
        n //= 10
    return True
    
def f():
    r = set()
    _, A = sys.stdin.readline(), set(map(int, sys.stdin.readline().split()))
    _, B = sys.stdin.readline(), set(map(int, sys.stdin.readline().split()))
    _, C = sys.stdin.readline(), set(map(int, sys.stdin.readline().split()))
    for a in A:
        for b in B:
            for c in C:
                if g(a+b+c):
                    r.add(a+b+c)
    return len(r)

T = int(sys.stdin.readline())
for _ in range(T):
    print(f())