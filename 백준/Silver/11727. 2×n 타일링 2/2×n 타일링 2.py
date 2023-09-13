li = [1, 1]
n = int(input())
for _ in range(n-1):
    li = [li[1],(li[1]+li[0]*2)%10007]
print(li[1])