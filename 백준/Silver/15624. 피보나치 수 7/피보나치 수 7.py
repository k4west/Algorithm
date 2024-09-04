def main():
    d = [0,1,1] + [-1] * 10**6
    m = 1000000007
    n = int(input())
    def f(n):
        if d[n]>=0: return d[n]
        if n % 2: d[n] = (pow(f(n//2+1), 2) + pow(f(n//2), 2)) % m
        else: d[n] = (pow(f(n//2+1), 2) - pow(f(n//2-1), 2)) % m
        return d[n]
    print(f(n))
if __name__ == "__main__":
    main()