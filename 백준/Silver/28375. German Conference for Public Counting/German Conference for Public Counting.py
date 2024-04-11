l = len(n := input())
a = (l - 1) * 10 + int(t := n[0])
if n < t * l:
    a -= 1
if l == 1:
    a += 1
print(a)