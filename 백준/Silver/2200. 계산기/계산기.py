input()
li = input().rstrip().split()
s = 2
for i in li[1:-1]:
    if i == "0":
        s += 2
    else:
        s += len(i) + 3
s += 1 + len(li[-1]) if li[-1] != "0" else 0
print(s)