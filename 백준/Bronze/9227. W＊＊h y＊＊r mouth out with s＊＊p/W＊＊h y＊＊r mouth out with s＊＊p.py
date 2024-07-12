import re
a = open(0).read().split('#')
dic, lines = a[0].split(), a[-2].strip().split('\n')
tmp = [' '.join([t[0]+'**'+t[3:] if len(t) > 3 and t[:4:3] in dic else t for t in line.split()]) for line in lines]
print('\n'.join(tmp))