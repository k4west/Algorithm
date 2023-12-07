import sys
input = sys.stdin.readline

def main():
    N = int(input())
    liq = sorted(list(map(int, input().split())))

    x = float('inf')
    s, e = 0, N-1
    l, r = 0, -1
    while s < e:
        t = liq[s]+liq[e]
        if t == 0:
            l, r = s, e
            break
        if t > 0:
            if x > t:
                x = t
                l, r = s, e
            e -= 1
        else:
            if x > -t:
                x = -t
                l, r = s, e
            s += 1
    print(liq[l], liq[r])

if __name__ == "__main__":
    main()