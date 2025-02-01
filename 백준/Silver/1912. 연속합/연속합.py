def main():
    n, *arr = map(int, open(0).read().split())
    t = m = arr[0]
    
    for i in range(1, n):
        t = max(arr[i], t+arr[i])
        m = max(m, t)
    
    print(m)
main()