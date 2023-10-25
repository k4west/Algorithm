import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    d = {0:0}
    for i in range(1, N+1):
        W, V = map(int, input().split())
        t = {}
        for v, w in d.items():
            if d.get(V+v, K+1) > W+w:
                t[V+v] = W+w
        d.update(t)

    print(max(d.keys()))
    
if __name__ == "__main__":
    main()