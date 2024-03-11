flag = False
a = list("".join(map(lambda x: x.lower(), open(0))))
for i, t in enumerate(a):
    if flag:
        if t in " ()\n": continue
        a[i] = t.upper()
        flag = False
    if t in ".!?": flag = True
print("".join(a))