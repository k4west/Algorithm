import sys
def f():
    global S
    op, *val = sys.stdin.readline().rstrip().split()
    if val:
        x = int(val[0])
    if op == "add":
        S.add(x)
    elif op == "remove":
        S -= {x}
    elif op == "check":
        print(int(x in S))
    elif op == "toggle":
        if x in S:
            S -= {x}
        else:
            S.add(x)
    elif op == "all":
        S = set(range(1,21))
    elif op == "empty":
        S.clear()
        
S = set()
T = int(sys.stdin.readline())
for _ in range(T):
    f()