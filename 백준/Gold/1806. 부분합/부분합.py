import sys
input = sys.stdin.readline 

def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    s = e = v = 0
    ans = N+1
    while e < N:
        v += arr[e]
        while v >= M:
            if (t:=e-s+1) < ans: ans = t
            v -= arr[s]
            s += 1
        e += 1
    if ans == N+1: print(0)
    else: print(ans)

if __name__ == "__main__":
    main()