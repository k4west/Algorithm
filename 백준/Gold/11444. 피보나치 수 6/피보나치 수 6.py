def main():
    d = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55, 11:89, 12:144, 13:233, 14:377, 15:610, 16:987, 17:1597}
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