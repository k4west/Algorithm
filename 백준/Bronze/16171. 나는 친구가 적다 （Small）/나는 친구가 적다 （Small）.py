import sys
import re

input = sys.stdin.readline
str1 = "".join(re.findall(r"[a-zA-Z]", input()))
str2 = input().rstrip()
print(int(str2 in str1))