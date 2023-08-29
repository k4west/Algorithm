s = input()
for i in range(len(s)//2):
    if s[i] != s[-(1+i)]:
        print(0)
        exit()
print(1)