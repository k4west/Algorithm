input()
s=input()
p=int(s[0])
a=[p]
for n in map(int,s[1:]):a.append(p^n);p=n
print(''.join(map(str,a)))