import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M, k, D = map(int, input().split())
    s, ans = k*N*M*(M-1)//2 + pow(M, 2)*N*(N-1)//2, -1
    if (b:=D//s) > 1:
        ans = s*b
    print(ans)