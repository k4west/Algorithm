def main():
    d = {1:1, 2:1}
    n = int(input())

    def f(n):
        if d.get(n):
            return d[n]
        if n % 2:
            d[n] = (pow(f(n//2+1), 2) + pow(f(n//2), 2)) % 1_000_000_007
        else:
            d[n] = (pow(f(n//2+1), 2) - pow(f(n//2-1), 2)) % 1_000_000_007
        return d[n]

    print(f(n))

if __name__ == "__main__":
    main()