import sys
input = sys.stdin.readline

def f(l, r):
    t = float('inf')
    ln, rn = len(l), len(r)
    for x in range(ln):
        u = l[x]
        y, z = 0, rn-1
        while y < z:
            if abs(t) > abs((v:=u+r[y]+r[z])):
                t, a, b, c = v, x, y, z
            if not v:
                return u, r[y], r[z]
            if v > 0:
                z -= 1
                continue
            y += 1
    tmp = [l[a], r[b], r[c], t]

    for z in range(rn):
        u = r[z]
        x, y = 0, ln-1
        while x < y:
            if abs(t) > abs((v:=l[x]+l[y]+u)):
                t, a, b, c = v, x, y, z
            if not v:
                return l[x], l[y], u
            if v > 0:
                y -= 1
                continue
            x += 1
    if t != tmp.pop():
        return l[a], l[b], r[c]
    return tmp
    
def main():
    N = int(input())
    liq = sorted(map(int, input().split()))
    for i in range(N-1):
        if liq[i] >= 0:
            break
    if not i: print(liq[0], liq[1], liq[2])
    elif i == N-1: print(liq[-3], liq[-2], liq[-1])
    else:
        a, b, c = f((l:=liq[:i]), (r:=liq[i:]))
        if len(l) > 3 and abs(l[-3]+l[-2]+l[-1]) < abs(a+b+c):
            a, b, c = l[-3], l[-2], l[-1]
        if len(r) > 3 and abs(r[0]+r[1]+r[2]) < abs(a+b+c):
            a, b, c = r[0], r[1], r[2]
        print(a, b, c)

if __name__ == "__main__":
    main()