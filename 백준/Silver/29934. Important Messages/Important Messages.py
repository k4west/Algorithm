def main():
    a = open(0)
    t = [next(a).strip() for _ in range(int(next(a)))]
    print(sum([next(a).strip() in t for _ in range(int(next(a)))]))
main()