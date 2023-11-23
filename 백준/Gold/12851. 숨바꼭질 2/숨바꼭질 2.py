import sys
input = sys.stdin.readline

def bfs(N, K):
    stack = [(K, 0)]
    M = 10**5+1
    v = [False]*(M)
    s, c = M, 0
    flag = 0

    if not N:
        N += 1
        flag = 1

    while stack:
        k, t = stack.pop(0)
        v[k] = True

        if k == N:
            if t <= s:
                s = t
                c += 1
            elif t > s:
                return "\n".join(map(str, (s+flag, c)))
            
        for i in (k-1, k+1, [k//2, -1][k%2]): 
            if 0 <= i < M and not v[i]:
                stack.append((i, t+1))
    return "\n".join(map(str, (s+flag, c)))

if __name__ == "__main__":
    N, K = map(int, input().split())
    M = 10**5+1
    v = [False]*(M)
    print(bfs(N, K))