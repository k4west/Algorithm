nums = [False for _ in range(10001)]
def gen(n):
    return n+(eval("+".join(str(n))))

for i in range(1, 10001):
    g = gen(i)
    if g < 10001: nums[g] = True

li = []
for i in range(1, 10001):
    if not nums[i]: li.append(i)

print("\n".join(map(str, li)))