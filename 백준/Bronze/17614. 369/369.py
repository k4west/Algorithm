n = int(input())
s = 0
for i in range(1, n + 1):
    i = str(i)
    s += i.count("3") + i.count("6") + i.count("9")
print(s)