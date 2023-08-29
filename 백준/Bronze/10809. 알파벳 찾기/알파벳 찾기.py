import string
s = input()
r = [s.index(a) if a in s else -1 for a in string.ascii_lowercase]
print(*r)