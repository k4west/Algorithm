N = input()
if N != '1':
    carry, i, ans = 0, 1, []
    for digit in map(int, N[::-1]):
        n, i = (digit - i) * 2 + carry, 0
        carry = n // 10
        ans.append(n % 10)
    if carry: ans.append(carry)
    print("".join(map(str, ans[::-1])))
else: print(N)