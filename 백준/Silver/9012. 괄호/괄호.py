import sys
T = int(sys.stdin.readline())
for _ in range(T):
    s = 0
    a = sys.stdin.readline().strip()
    for i in a:
        if i == "(":
            s += 1
        else:
            if s:
                s -= 1
            else: 
                s = 1
                break
    if s:
        print("NO")
    else: print("YES")