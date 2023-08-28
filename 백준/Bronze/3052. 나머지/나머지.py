s = set()
for i in open(0):
    s.add(int(i)%42)
print(len(s))