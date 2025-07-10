s = input()
for c in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(c, ' ')
print(len(s))