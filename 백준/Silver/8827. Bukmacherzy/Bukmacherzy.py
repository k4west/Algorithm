ans = []
tmp = ["NIE", "TAK"]
for _ in range(int(input())):
    X, Y = map(float, input().split())
    ans.append(tmp[(X - 1) * (Y - 1) > 1])
print("\n".join(ans))