k = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == k: k = b
    elif b == k: k = a
print(k)