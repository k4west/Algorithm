import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    mc = sorted(zip(map(int, input().split()), map(int, input().split())), reverse=True)
    d = {0:0}
    for i in range(N):
        m, c = mc[i]
        t = {}
        for dc, dm in d.items():
            tm, tc = min(M, m+dm), c+dc
            if d.get(tc, 0) < tm:
                t[tc] = tm
        d.update(t)
    print(min(c for c, m in d.items() if m==M))

if __name__ == "__main__":
    main()