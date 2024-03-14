input()
s = 0
for i in input().split()[1:]:
    s += len(i) + 3
    if i == "0": s -= 2
print(s)