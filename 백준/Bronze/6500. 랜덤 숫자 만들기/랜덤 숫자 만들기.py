def main():
    n = 4
    ans = []
    for a in map(int, open(0)):
        if a == 0:
            break
        visit = set()
        while a not in visit:
            visit.add(a)
            a *= a
            a = int(str(a).zfill(8)[2:6])
        ans.append(len(visit))
    print("\n".join(map(str, ans)))

main()