import sys
input = sys.stdin.readline

def main():
    N, S = map(int, input().split())
    *arr, = map(int, input().split())
    l, r, m = {}, {}, N//2

    def f(li, s, a, d):
        d[s] =  d.get(s, 0) + 1
        for i in range(a, len(li)):
            f(li, s + li[i], i+1, d)

    f(arr[:m], 0, 0, l)
    f(arr[m:], 0, 0, r)
    c = 0
    if not S: c = -1

    for lk in l:
        if (rk:=S-lk) in r:
            c += l[lk] * r[rk]
    print(c)

if __name__ == "__main__":
    main()