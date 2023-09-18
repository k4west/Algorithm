import sys
li = [[0], [0]]
for _ in range(3):
    a, b = sys.stdin.readline().split()
    if a in li[0]:
        li[0].remove(a)
    else: li[0].append(a)
    if b in li[1]:
        li[1].remove(b)
    else: li[1].append(b)
print(li[0][1], li[1][1])