import sys

input = sys.stdin.readline
ans = []

time = 80

li = [
    list(map(lambda x: float(x) if "." in x else x, input().split()))
    for _ in range(int(input()))
]
li.sort(key=lambda x: (x[2], x[1]))
for i, t, _ in li:
    c = 1
    tmp = [i]
    for j, _, b in li:
        if i == j:
            continue
        t += b
        c += 1
        tmp.append(j)
        if c == 4:
            break
    if time > t:
        time = t
        ans = tmp

print(time)
print(*ans, sep="\n")