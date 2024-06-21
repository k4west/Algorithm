a=[]
c={'kg':'lb','lb':'kg','l':'g','g':'l'}
d={'kg':2.2046,'lb':0.4536,'l':	0.2642,'g':	3.7854}
for i in [*open(0)][1:]:
    s, t = i.strip().split()
    a.append(f'{float(s)*d[t]:.4f} {c[t]}')
print('\n'.join(a))