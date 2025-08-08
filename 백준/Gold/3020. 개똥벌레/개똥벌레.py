def bi(target, li):
    s, e = 0, N//2-1
    
    while s <= e:
        m = (s+e)//2
    
        if li[m] < target:
            s = m+1
        else:
            e = m-1
    
    return s

N, H = map(int, input().split())
li1, li2 = [], []

for _ in range(N//2):
    li1.append(int(input()))
    li2.append(int(input()))

li1.sort()
li2.sort()

ob = [0]*H
for i in range(H):
    ob[i] = N - bi(i+1, li1) - bi(H-i, li2)


min_val = 200000
cnt = 0
for c in ob:
    if min_val > c:
        min_val = c
        cnt = 1
    elif min_val == c:
        cnt += 1

print(min_val, cnt)