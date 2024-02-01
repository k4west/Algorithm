N = int(input())
facotrs = {}
for n in map(int, input().split()):
    tmp = {}
    for d in range(2, n + 1):
        while n % d == 0:
            n /= d
            if d in tmp:
                tmp[d] += 1
            else:
                tmp[d] = 1
        if n == 1:
            break
    for d, count in tmp.items():
        facotrs[d] = max(facotrs.get(d, 0), count)

num = 1
for i, j in facotrs.items():
    num *= i**j

if len(facotrs) == 1:
    num *= i

print(num)