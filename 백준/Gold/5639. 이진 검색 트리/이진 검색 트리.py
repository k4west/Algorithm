import sys
sys.setrecursionlimit(10000*2)

def main():
    li = [int(n) for n in open(0).readlines()]

    def f(s, e):
        if s >= e: 
            print(li[s])
            return
        if li[s] > li[e] or li[s] < li[s+1]:
            f(s+1, e)
        else:
            for i in range(s+1, e+1):
                if li[s] < li[i]:
                    f(s+1, i-1)
                    f(i, e)
                    break
        print(li[s])

    f(0, len(li)-1)

if __name__ == "__main__":
    main()