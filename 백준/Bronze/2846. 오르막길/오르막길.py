input()
li = list(map(int, input().split()))
bottom = li[0]
top = li[0]
ans = 0
for h in li[1:]:
    if top >= h:
        if ans < (high := top - bottom):
            ans = high
        bottom = h
        top = h
    else:
        top = h
if ans < (high := top - bottom):
    ans = high
print(ans)