def check(s):
    prev = s[0]
    ps = {prev}
    for i in s[1:]:
        if i != prev:
            if i not in ps:
                ps.add(i)
                prev = i
            else:
                return False
    return True

c = 0
for _ in range(int(input())):
    if check(input()):
        c += 1
print(c)