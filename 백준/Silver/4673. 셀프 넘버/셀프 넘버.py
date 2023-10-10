def gen(n):
    return {n+(eval("+".join(str(n))))}

nums = set(range(1, 10001))
for i in range(1, 10001):
    nums -= gen(i)

print("\n".join(map(str, sorted(nums))))