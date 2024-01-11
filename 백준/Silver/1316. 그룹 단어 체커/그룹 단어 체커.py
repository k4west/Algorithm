n = int(input())
for _ in range(n):
    string = input()
    t = string[0]
    v = {t}
    flag = False
    for s in string:
        if s != t:
            if s in v:
                flag = True
                break
            v.add(s)
            t = s
    if flag:
        n -= 1
print(n)