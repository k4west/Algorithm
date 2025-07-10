N, X = map(int, input().split())
li = []
for i in map(int, input().split()):
    if i < X:
        li.append(i)
print(*li)