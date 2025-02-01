def main():
    a = open(0)
    t = m = -1000
    next(a)
    for i in map(int, next(a).split()):
        t = t*(t>0) + i
        if m < t: m = t
    print(m)
main()