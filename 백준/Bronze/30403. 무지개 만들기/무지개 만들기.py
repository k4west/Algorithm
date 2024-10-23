r = 'ROYGBIV'
s = set(open(0).read()[1:])
lr = not set(r) - s
sr = not set(r.lower()) - s
print(('NO!', 'YES', 'yes', 'YeS')[lr+2*sr])