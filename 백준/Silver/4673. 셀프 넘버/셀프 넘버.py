def gen(n):
    s = n
    while n:
        s += n%10
        n //= 10
    return {s}

nums = set(range(1, 10001))
for i in range(1, 10001):
    nums -= gen(i)

print("\n".join(map(str, sorted(nums))))