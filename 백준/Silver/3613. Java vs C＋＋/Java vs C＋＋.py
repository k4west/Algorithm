import sys
s = sys.stdin.readline().rstrip()
if "__" in s or s[0].isupper() or s[0] == "_" or s[-1] == "_":
    print("Error!")
elif '_' in s:
    if not s.replace("_", "").islower():
        print("Error!")
    else:
        s = s[0] + s.title()[1:]
        print(s.replace("_", ""))
else:
    a = list(s)
    for i in range(1, len(a)):
        if a[i].isupper():
            a[i] = "_" + a[i].lower()
    print("".join(a))