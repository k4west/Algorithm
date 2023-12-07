import sys
input = sys.stdin.readline

def main():
    N = int(input())
    liq = sorted(list(map(int, input().split())))

    s, e = 0, N-1
    l, r = 0, -1
    x = liq[s]+liq[e]
    while s < e:
        t = liq[s]+liq[e]
        if abs(t) < abs(x):
            x = t
            l, r = s, e
        if t == 0:
            break
        if t > 0:
            e -= 1
            continue
        s += 1
    print(liq[l], liq[r])

if __name__ == "__main__":
    main()