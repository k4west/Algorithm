input()
t = 0
c = 0
m = 1000
for i in map(int, input().split()):
    if i%2:
        c += 1
        if m > i:
            m = i
    t += i
if c%2:
    t -= m
print(t)