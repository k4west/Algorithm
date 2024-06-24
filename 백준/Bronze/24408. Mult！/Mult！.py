i=0
for n in open(0).readlines()[1:]:
    n=int(n)
    if not i:i=n
    elif not n%i:print(n);i=0