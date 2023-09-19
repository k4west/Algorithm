import sys
def f(N, G, V):
    c = 0
    for n in range(1,N+1):
        if not V[n]:
            c += 1
            V[n] = True
            li = [n]
            while li:
                s = li.pop(0)
                for t in G[s]:
                    if not V[t]:
                        V[t] = True
                        li.append(t)
    print(c)

def g(N, M):
    G = [[] for _ in range(N+1)]
    V = [False] * (N+1)
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        G[i].append(j)
        G[j].append(i)
    f(N, G, V)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    g(N, M)