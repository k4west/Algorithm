import sys
input = sys.stdin.readline
ans = []
d = {i: str(i) for i in range(10)}
for i in range(65, 91):
    d[i - 55] = chr(i)
for _ in range(int(input())):
    x, y, z = input().split()
    z = int(z, int(x))
    if not z:
        ans.append(str(z))
    else:
        y = int(y)
        tmp = ""
        while z:
            tmp += d[z % y]
            z //= y
        ans.append(tmp[::-1])
print("\n".join(ans))