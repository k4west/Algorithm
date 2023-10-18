def main():
    A, B = map(int, input().split())

    c = 1
    while A < B:
        if not B%2: B //= 2
        elif B%10 == 1: B //= 10
        else: break
        c += 1

    if A == B: print(c)
    else: print("-1")

if __name__ == "__main__":
    main()