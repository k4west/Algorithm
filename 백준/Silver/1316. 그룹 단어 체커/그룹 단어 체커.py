n = int(input())
c = 0
for i in range(n):
    sr = list(input())
    st = list(set(sr))
    for j in st:
        a = sr.index(j)
        b = sr.count(j)
        if b != 1 and sr[a: a + b] != [j] * b:
            c += 1
    if c != 0:
        n -= 1
    c = 0
print(n)