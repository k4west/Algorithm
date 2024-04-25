a = open(0)
n = m = 0
for i in a:
    off_, on_ = map(int, i.split())
    n += on_ - off_
    if m < n:
        m = n
print(m)