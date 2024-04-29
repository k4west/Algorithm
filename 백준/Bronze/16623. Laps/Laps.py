def main():
    a = open(0)
    next(a)
    c = prev = 0
    for d in map(int, next(a).split()):
        if prev > d: c += 1
        prev = d
    print(c)
main()