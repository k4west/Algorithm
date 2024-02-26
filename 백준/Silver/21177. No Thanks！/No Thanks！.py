a = open(0)
next(a)
cards = sorted(map(int, next(a).split()))
score = 0
prev = -1
for num in cards:
    if prev + 1 != num: score += num
    prev = num
print(score)