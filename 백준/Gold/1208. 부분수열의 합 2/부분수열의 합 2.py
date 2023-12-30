import sys
input = sys.stdin.readline

def main():
    N, S = map(int, input().split())
    *arr, = map(int, input().split())
    m = N//2

    def fl(li):
        t = [0]
        for a in li:
            tmp = [a+b for b in t]
            t.extend(tmp)
        return  t
    
    def fd(li, s, a, d):
        d[s] =  d.get(s, 0) + 1
        for i in range(a, len(li)):
            fd(li, s + li[i], i+1, d)


    l = fl(arr[:m])
    r = {}
    fd(arr[m:], 0, 0, r)
    
    c = 0
    if not S: c = -1

    for lk in l:
        if (rk:=S-lk) in r:
            c += r[rk]
    print(c)

if __name__ == "__main__":
    main()