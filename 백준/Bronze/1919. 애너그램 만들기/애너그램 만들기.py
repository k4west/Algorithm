from collections import Counter
n = (Counter(str1 := input()) & Counter(str2 := input())).total()
print(len(str1) + len(str2) - 2 * n)