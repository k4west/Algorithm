r = 'ROYGBIV'
s = set(open(0).read()[1:])
print(('NO!', 'YES', 'yes', 'YeS')[(not set(r) - s) + 2*(not set(r.lower()) - s)])