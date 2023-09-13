li = [1, 1]
n = int(input())
for _ in range(n-1):
    li.append((li[-1]+li[-2]*2)%10007)
print(li[-1])