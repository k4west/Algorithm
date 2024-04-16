def main():
    ans = []
    for i, s in enumerate(open(0)):
        cnt = 0
        d = 0
        for b in s.rstrip():
            if b == "}":
                if d <= 0:
                    cnt += 1
                    d += 1
                else: d -= 1
            else: d += 1
        cnt += abs(d) // 2
        ans.append(f"{i+1}. {cnt}")
    print("\n".join(ans[:-1]))
main()