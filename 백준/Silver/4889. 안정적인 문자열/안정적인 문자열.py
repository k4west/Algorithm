def main():
    ans = []
    for i, s in enumerate(open(0)):
        cnt = 0
        d = [0, 0]
        for b in s.rstrip():
            j = 0
            if b == "}":
                if d[0] == d[1]:
                    cnt += 1
                else:
                    j += 1
            d[j] += 1
        cnt += abs(d[0] - d[1]) // 2
        ans.append(f"{i+1}. {cnt}")
    print("\n".join(ans[:-1]))
main()