import sys
sys.setrecursionlimit(10**6)

def main():
    li = [int(n) for n in open(0).readlines()]

    def f(s, e):
        if s > e: return
        for i in range(s+1, e+1):
            if li[s] < li[i]:
                f(s+1, i-1)
                f(i, e)
                break
        else: f(s+1, e)
        print(li[s])

    f(0, len(li)-1)

if __name__ == "__main__":
    main()