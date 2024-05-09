a = open(0)
h, w = map(int, next(a).split())
c = s = 0
l = r = -1
for i, col in enumerate(zip(*a.readlines())):
    if i == w: break
    b = h-col.count('.')
    if b:
        c += b
        s += i*b
        if col[-1] != '.':
            if l == -1: l = i
            r = i
if (s:=s/c) < l-.5: print('left')
elif s > r+.5: print('right')
else: print('balanced')