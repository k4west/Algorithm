def main():
    n, *a = open(0)
    n = int(n)
    t = 0
    prev = 10001
    condo = sorted([[*map(int, i.split())] for i in a])
    for _, c in condo:
        if c < prev: prev = c; t += 1
    print(t)
main()