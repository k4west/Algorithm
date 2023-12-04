def main():
    N = int(input())
    liq = list(map(int, input().split()))

    if liq[0] >= 0:
        return liq[:2]
    if liq[-1] <= 0:
        return liq[-2:]
    
    def f():
        for i in range(N):
            if liq[i] >= 0:
                if i >= 2:
                    tmp = liq[i-2:i]
                    a = -sum(tmp)
                    if i < N-2 and (b:=sum(liq[i:i+2])) < a:
                        a = b
                        tmp = liq[i:i+2]
                    return i-1, i, a, tmp
                else:
                    return i-1, i, sum(liq[i:i+2]), liq[i:i+2]

    s, e, m, ans = f()
    while True:
        t = liq[s]+liq[e]
        if t == 0:
            ans = [liq[s], liq[e]]
            break
        if t > 0:
            if m > t:
                m = t
                ans = [liq[s], liq[e]]
            if not s: break
            s -= 1
        else:
            if m > -t:
                m = -t
                ans = [liq[s], liq[e]]
            if e == N-1: 
                break
            e += 1
    return ans

if __name__ == '__main__':
    print(*main())