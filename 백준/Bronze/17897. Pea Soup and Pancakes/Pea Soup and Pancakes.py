a=open(0)
r='Anywhere is fine I guess'
s={'pea soup','pancakes'}
for _ in range(int(next(a))):
    n=int(next(a))
    name=next(a)
    if not s-{next(a).strip() for _ in range(n)}:
        r=name
        break
print(r)