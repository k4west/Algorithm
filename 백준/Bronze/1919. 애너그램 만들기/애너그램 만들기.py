str1, str2 = input(), input()
for s in str1:
    if s in str2: str1, str2 = str1.replace(s, "", 1), str2.replace(s, "", 1)
print(len(str1 + str2))