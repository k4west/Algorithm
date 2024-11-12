def main():
    ans = []
    a = open(0)
    for _ in range(int(next(a))):
        n = int(next(a))
        li = [0] + list(map(int, next(a).split()))
        d = [0]*(n+1)
        for i in li: d[i] += 1
        left = [i for i in range(1, n+1) if not d[i]]
        for i in left:
            d[(j:=li[i])] -= 1
            if not d[j]: left.append(j)
        ans.append(len(left))
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()