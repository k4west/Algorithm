s=input()
t='ABCDF'
for i in range(3):
    if t[i] in s:
        for j in t[i+1:]:s=s.replace(j,t[i])
        break
else:s='A'*len(s)
print(s)