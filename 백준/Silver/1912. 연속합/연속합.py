def main():
    a = open(0)
    t = m = float('-inf')
    next(a)
    for i in map(int, next(a).split()):
        t = max(i, t+i)
        if m < t: m = t
    print(m)
main()