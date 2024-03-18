def is_palindrome(n):
    if len(n) < 2 or n == n[::-1]:
        return True
    return False


def b_format(n, b):
    m = 1
    nb = []
    while True:
        nb.append(n % (m * b) // m)
        n -= nb[-1] * m
        m *= b
        if n < m:
            break
    return "".join(map(str, nb))[::-1]


n = int(input())
ans = []
for b in range(2, 11):
    nb = b_format(n, b)
    if is_palindrome(nb):
        ans.append(str(b) + " " + nb)
if ans:
    print("\n".join(ans))
else:
    print("NIE")