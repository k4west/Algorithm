def gen(n):
    return n+(eval("+".join(str(n))))

nums, gens = set(range(1, 10001)), set()
i = 1
for i in range(1, 10001):
    gens.add(gen(i))

nums -= gens
print("\n".join(map(str, sorted(nums))))