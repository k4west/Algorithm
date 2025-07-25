heights = [int(input()) for _ in range(9)]
s = sum(heights)
li = []

for i in range(8):
    for j in range(i+1, 9):
        if s == 100 + heights[i] + heights[j]:
            li = [heights[k] for k in range(9) if k != i and k != j]
            break
    if li:
        break

li.sort()
print(*li, sep='\n')