f=False
a=list("".join(map(lambda x:x.lower(),open(0))))
for i,t in enumerate(a):
    if f:
        if t in " ()\n":continue
        a[i]=t.upper()
        f=False
    if t in ".!?":f=True
print("".join(a))