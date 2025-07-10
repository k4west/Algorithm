N = int(input())
m, *arr = map(int, input().split())
M = m
for i in arr:
    if i < m:
        m = i
    elif i > M:
        M = i
print(m, M)