doc = input()
wod = input()

i, count = 0, 0
n = len(wod)
while i + n - 1 <= len(doc):
    if wod == doc[i:i+n]:
        count += 1
        i += n
    else: i += 1
print(count)