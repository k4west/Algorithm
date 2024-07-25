def main():
    n, *a = map(int, open(0).read().strip().split())
    a.sort(reverse=True) 
    s = t = 0
    for i in a:
        s += 1
        if s <= i:
            t = s
    print(t)
main()