_, *a = open(0).read().split()
t = []
for i in a:
    A, B = map(int, i.split(','))
    t.append(A+B)
print('\n'.join(map(str, t)))