def main():
    n, *arr = map(int, open(0).read().split())
    arr.sort()
    s = sum(arr) + sum(arr[(n+1)//2:]) - sum(arr[:n//2])
    print(s)

if __name__ == "__main__":
    main()