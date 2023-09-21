*li, = map(int, open(0).read().split())
e = 0
print(sum((e:=b) and 1 for b, a in sorted(zip(li[2::2], li[1::2])) if e <= a))
