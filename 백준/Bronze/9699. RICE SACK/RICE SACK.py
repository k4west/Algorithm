ans = []
for i in range(int(next(a:= open(0)))):
    m = 0
    for s in map(int, next(a).split()):
        if m < s:
            m = s
    ans.append(f'Case #{i+1}: {m}')
print('\n'.join(ans))