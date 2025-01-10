a, b = input().split()
n = max(map(len, (a, b)))
carry = 0
t = []
for i, j in zip(a.zfill(n)[::-1], b.zfill(n)[::-1]):
    k = int(i) + int(j) + carry
    carry, r = k//10, k%10
    t.append(r)
if carry:
    t.append(carry)
print("".join(map(str, t[::-1])))