import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    a = eval("+".join(sys.stdin.readline().split()))
    i = 1
    while 1:
        if a > n:
            print(i)
            break
        a *= 4
        i += 1