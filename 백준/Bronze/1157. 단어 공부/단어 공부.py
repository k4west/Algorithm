s = input().lower()
M, c = '', 0
for i in range(26):
    if c < (t:=s.count(chr(i+97))):
        M = chr(i+65)
        c = t
    elif c == t:
        M = '?'
print(M)