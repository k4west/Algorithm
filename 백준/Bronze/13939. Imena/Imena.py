input()
for s in input().replace("?", ".").replace("!", ".").split(".")[:-1]: print(sum((True for t in s.replace(".", "").split() if t.isalpha() and t[0] == t[0].upper() and t[1:] == t[1:].lower())))