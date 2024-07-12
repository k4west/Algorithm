import re
a = open(0).read().split('#')
dic, lines = a[0].split(), a[-2].strip().split('\n')
def clean(text):
    return ' '.join([t[0]+'**'+t[3:] if len(t) > 3 and t[:4:3] in dic else t for t in text.split()])
tmp = [clean(line) for line in lines]
print('\n'.join(tmp))