import sys
input = sys.stdin.readline

def main():
    N = int(input())
    liq = sorted(map(int, input().split()))
    for i in range(N-1):
        if liq[i] >= 0:
            break
    if not i: print(liq[0], liq[1], liq[2])
    elif i == N-1: print(liq[-3], liq[-2], liq[-1])
    else:
        ans = float('inf')
        for x in range(0, N-2):
            u = liq[x]
            y, z = x + 1, N-1
            while y < z:
                if abs(ans) > abs((v:=u+liq[y]+liq[z])):
                    ans, a, b, c = v, x, y, z
                if not v:
                    print(liq[a], liq[b], liq[c])
                    return
                if v > 0:
                    z -= 1
                    continue
                y += 1
        print(liq[a], liq[b], liq[c])
    
if __name__ == "__main__":
    main()