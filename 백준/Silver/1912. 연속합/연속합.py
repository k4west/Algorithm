n = int(input())
*li, = map(int, input().split())

for i in range(1, n):
    if li[i-1] > 0:
        li[i] += li[i-1]

print(max(li))