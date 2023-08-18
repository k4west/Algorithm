full_name = input()
upper_name = "".join(s for s in full_name if s.isupper())
i = 0
UCPC = "UCPC"
for u in upper_name:
    if u == UCPC[i]:
        i += 1
        if i == 4:
            print("I love UCPC")
            exit()
print("I hate UCPC")