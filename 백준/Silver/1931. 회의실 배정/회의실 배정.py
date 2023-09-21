def f():
    c = open(0)
    next(c)
    *li, = map(int, c.read().split())
    e = 0
    print(sum((e:=b) and 1 for b, a in sorted(zip(li[1::2], li[::2])) if e <= a))
if __name__ == "__main__": f()