from sys import stdin
input = stdin.readline

def main():
    N, K = map(int, input().split())
    q = [(K, 0)]
    v = set()

    while True:
        s, t = q.pop(0)
        if s == N:
            print(t)
            break
        if not s%2 and (d:=s//2) not in v and s > N:
            v.add(d)
            q.append((d, t))
        for i in (s+1, s-1):
            if i not in v:
                v.add(i)
                q.append((i, t+1))

if __name__ == "__main__":
    main()