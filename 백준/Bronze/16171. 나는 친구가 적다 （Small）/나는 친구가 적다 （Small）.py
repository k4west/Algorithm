import re
str1 = "".join(re.findall(r"[a-zA-Z]", input()))
str2 = input()
print(int(str2 in str1))