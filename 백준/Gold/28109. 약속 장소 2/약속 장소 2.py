def main():
    a = open(0)
    N, K = map(int, next(a).split())
    S = next(a).strip()

    S = list(S)
    for i in range(N):
        if K <= (t:=ord(S[i])-65):
            S[i] = chr(64+K)
            return S
        K -= t
    if K==1:
        return S
    K -= 1
    for i in range(1, N+1):
        if K <= 90-(t:=ord(S[N-i])):
            S[N-i] = chr(t+K)
            return S
        K -= 90-t
    return "-1"
print("".join(main()))