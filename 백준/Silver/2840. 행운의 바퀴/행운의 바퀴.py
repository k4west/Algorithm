def main():
    a = open(0)
    N, K = map(int, next(a).split())
    visit = set()
    wheel = ['?' for _ in range(N)]
    idx = 0
    for _ in range(K):
        S, alpha = map(lambda x: x.strip(), next(a).split())
        S = int(S) % N
        idx = (idx - S) % N
        if wheel[idx] == "?":
            if alpha in visit:
                return "!"
            visit.add(alpha)
            wheel[idx] = alpha
        elif wheel[idx] != alpha:
            return "!"
    return ''.join((wheel*2)[idx:idx+N])

if __name__=="__main__":
    print(main())
