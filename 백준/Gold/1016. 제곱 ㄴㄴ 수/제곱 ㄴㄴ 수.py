def main():
    x, y = map(int, input().split())
    arr = [True for _ in range(y-x+1)]
    for i in map(lambda x:x**2, range(2, int(y**.5)+1)):
        s = i-x%i if x%i else 0
        for j in range(s, y-x+1, i):
            arr[j] = False
    print(sum(arr))
if __name__ == "__main__":
    main()