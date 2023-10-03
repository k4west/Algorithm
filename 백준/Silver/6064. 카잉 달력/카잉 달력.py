import sys
def main():
    T = range(int(sys.stdin.readline()))
    for _ in T:
        M, N, x, y = map(int, sys.stdin.readline().split())
        # k을 M으로 나누면 나머지가 x 이고
        # k을 N으로 나누면 나머지가 y입니다.
        k = x
        while k <= M*N:
            if k%M==x%M and k%N==y%N:
                print(k)
                break
            k += M
        if k > M*N: print(-1)
if __name__=="__main__":
    main()