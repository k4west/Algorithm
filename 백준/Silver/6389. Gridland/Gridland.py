t = []
r = 0.41
_, *a = open(0)
for i, j in enumerate(a, 1):
    m, n = map(int, j.split())
    t.append(f'Scenario #{i}:\n{m*n + m%2*n%2*r:.2f}')
print('\n\n'.join(t))