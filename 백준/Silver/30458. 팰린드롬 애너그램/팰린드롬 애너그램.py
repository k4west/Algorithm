n,s=open(0)
n=int(n)//2
s=s.strip()
s=s[:n]+s[-n:]
def f():
    for i in map(chr,range(97, 123)):
        if s.count(i)%2:
            return 'No'
    return 'Yes'
print(f())
