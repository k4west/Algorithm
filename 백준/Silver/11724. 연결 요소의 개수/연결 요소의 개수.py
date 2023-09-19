import sys
def f(N, M):
    c, t = N, 1
    li = [0 for _ in range(N+1)]
    for _ in range(M):
        if c == 1: break
        i, j = map(int, sys.stdin.readline().split())
        if li[i] * li[j] == 0:
            if li[i] == li[j]:
                li[i] = li[j] = t
                t += 1
            else:
                li[i] = li[j] = li[i]+li[j]
        elif li[i] != li[j]:
            s = min(li[i], li[j])
            l = max(li[i], li[j])
            for k in range(1, N+1):
                if li[k] == l:
                    li[k] = s
        else: c += 1
        c -= 1
    print(c)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    f(N, M)