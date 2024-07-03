a=open(0)
d={}
for _ in range(int(next(a))):
    lang, *line = next(a).strip().split()
    for word in line:
        d[word.lower()] = lang
t=[]
for i in a.readlines()[1:]:
    sep = [j for j in ' ,.;!?()' if j in i]
    sample=[i.strip().lower()]
    for s in sep:
        sample = [p.split(s) for p in sample]
        sample.append([])
        sample = sum(sample, [])
    for word in sample:
        word = word.lower()
        if word in d:
            t.append(d[word])
            break
print('\n'.join(t))