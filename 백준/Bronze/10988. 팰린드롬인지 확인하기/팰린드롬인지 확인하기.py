s = input()
p = 1
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        p = 0
        break
print(p)