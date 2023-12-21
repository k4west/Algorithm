import sys
input = sys.stdin.readline
    
def main():
    T = int(input())
    n, A = int(input()), list(map(int, input().split()))
    m, B = int(input()), list(map(int, input().split()))

    Tsub = {}
    for i in range(n):
        asum = 0
        for j in range(i, n):
            asum += A[j]
            if asum in Tsub:
                Tsub[asum] += 1
            else:
                Tsub[asum] = 1
        
    ans = 0
    for i in range(m):
        bsum = 0
        for j in range(i, m):
            bsum += B[j]
            if T-bsum in Tsub:
                ans += Tsub[T-bsum]

    print(ans)

if __name__ == "__main__":
    main()