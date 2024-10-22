_, *a = open(0)
s = 2**.5
t = []
for i in a:
    r, b = map(int, i.split())
    t.append(f'{2*r*r:.3f}' if s*r <= b else f'{b*(((2*r+b)*(2*r-b))**.5):.3f}')
print('\n'.join(map(str, t)))