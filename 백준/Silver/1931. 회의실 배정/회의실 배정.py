def f(c=0):
    a = open(0)
    *li, = map(int, a.read().split())
    print(sum((c:=e) and 1 for e, s in sorted(zip(li[2::2], li[1::2])) if c <= s))
if __name__ == "__main__": f()