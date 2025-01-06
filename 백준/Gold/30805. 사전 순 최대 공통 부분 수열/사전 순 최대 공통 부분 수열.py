def main():
    N = int(input())
    *A, = map(int, input().split())
    M = int(input())
    *B, = map(int, input().split())
    a = [[] for _ in range(101)]
    b = [[] for _ in range(101)]
    for i in range(max(N, M)):
        if i < N:
            a[A[i]].append(i)
        if i < M:
            b[B[i]].append(i)
    
    aidx = bidx = -1
    c = 0
    C = []
    for i in range(100, 0, -1):
        if a[i] and b[i]:
            ta = [t for t in a[i] if t > aidx]
            tb = [t for t in b[i] if t > bidx]
            if (t:= min(map(len, (ta, tb)))):
                c += t
                C.extend([i]*t)
                aidx = ta[t-1]
                bidx = tb[t-1]
    print(c)
    print(*C)
main()