n = int(input())
a = [[0 for i in range(100)] for j in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for s in range(x, x + 10):
        for t in range(y, y + 10):
            a[s][t] = 1
print(sum(sum(a,[])))