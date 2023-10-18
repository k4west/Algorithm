import sys
T = range(int(sys.stdin.readline()))
li = []
for _ in T:
    flag, e = 0, False
    fns = sys.stdin.readline().replace("RR","").rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    if arr == [""]: arr = []
    for fn in fns:
        if fn == "R":
            flag = (flag + 1)%2
        elif arr:
            arr.pop(-flag)
        else:
            e = True
            li.append("error")
            break
    if not e:
        if not flag: flag = -1
        li.append("["+",".join(arr[::-flag])+"]")
print("\n".join(li))