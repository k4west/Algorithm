def main():
    a = open(0)
    t = {next(a).strip() for _ in range(int(next(a)))}
    s = 0
    for _ in range(int(next(a))):
        s += next(a).strip() in t
    print(s)
main()