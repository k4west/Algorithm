ans = []
for i in range(int(input())):
    L, n = map(int, input().split())
    roots = [0] + list(map(int, input().split()))
    m = 0
    while L > 0:
        L = roots[L]
        m += 1

    ans.append(f"Data Set {i+1}:\n{m}\n")
print(*ans, sep="\n")