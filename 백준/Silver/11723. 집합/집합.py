import sys
def f(S):
    op, *val = sys.stdin.readline().rstrip().split()
    if op == "add":
        S.add(int(val[0]))
    elif op == "remove":
        S.discard(int(val[0]))
    elif op == "check":
        if int(val[0]) in S:
            print(1)
        else: print(0)
    elif op == "toggle":
        x = int(val[0])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif op == "all":
        S.update(range(1,21))
    elif op == "empty":
        S.clear()
    return S
        
S = set()
T = int(sys.stdin.readline())
for _ in range(T):
    S = f(S)