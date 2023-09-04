import sys
def f():
    sys.stdin.readline()
    C = map(int, sys.stdin.readline().split())
    P = sys.stdin.readline().strip()

    EC = [0] * 53
    for c in C:
        EC[c] += 1

    k = 1
    for p in P:
        if p == " ":
            t = 32
        elif p.islower():
            t = 70
        else: t = 64
        p = ord(p)
        p -= t
        EC[p] -= 1
        
    for i in range(53):
        if EC[i] < 0:
            return 'n'
    return 'y'
print(f())