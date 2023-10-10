nums = [False for _ in range(10001)]
def gen(n):
    s = n
    while n:
        s += n%10
        n //= 10
    return s

for i in range(1, 10001):
    g = gen(i)
    if g < 10001: nums[g] = True

li = []
for i in range(1, 10001):
    if not nums[i]: li.append(i)

print("\n".join(map(str, li)))