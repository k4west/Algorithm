a=open(0)
d={}
for _ in range(int(next(a))):
    lang, *line = next(a).strip().split()
    for word in line:
        d[word.lower()] = lang
t=[]
for i in a.readlines()[1:]:
    for j in ',.!?;()':
        i=i.replace(j, ' ')
    sample=i.strip().lower().split()
    for word in sample:
        word = word.lower()
        if word in d:
            t.append(d[word])
            break
print('\n'.join(t))