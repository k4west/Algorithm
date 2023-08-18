s=input()
l=['c=','c-','dz=','d-','lj','nj','s=','z=']
c=0
for i in l:
    while i in s:
        s=s.replace(i," ",1)
        c+=1
print(len(s))