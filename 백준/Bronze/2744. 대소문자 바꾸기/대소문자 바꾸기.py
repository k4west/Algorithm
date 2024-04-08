s=''
for t in input():
    if t == t.lower():
        s += t.upper()
    else:
        s += t.lower()
print(s)