import sys
from collections import Counter
input = sys.stdin.readline

def main():
    N, S = map(int, input().split())
    arr = tuple(map(int, input().split()))
    m = N//2

    def f(li):
        t = [0]
        for a in li:
            tmp = [a+b for b in t]
            t.extend(tmp)
        return  t

    l = f(arr[:m])
    r = Counter(f(arr[m:]))
    
    c = 0
    if not S: c = -1

    for lk in l:
        if (rk:=S-lk) in r:
            c += r[rk]
    print(c)

if __name__ == "__main__":
    main()