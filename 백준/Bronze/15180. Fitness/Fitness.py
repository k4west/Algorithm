a = open(0)
t = [int(next(a).strip())]
flag = False
while (s:=next(a).strip())!='#':
    c, n = s
    if c=='A':
        i = (t[-1] - int(n)) % 8 or 8
    else:
        i = (t[-1] + int(n)) % 8 or 8
    if i in t:
        flag = True
    t.append(i)
if len(set(t)) < 5 or flag:
    t.append('reject')
print(' '.join(map(str, t)))