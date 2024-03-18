def is_palindrome(n):
    if len(n) < 2 or n == n[::-1]:
        return True
    return False


def b_format(n, b):
    nb = ""
    while n:
        n, m = n // b, n % b
        nb += str(m)
    return "".join(nb)[::-1]


n = int(input())
ans = []
for b in range(2, 11):
    nb = b_format(n, b)
    if is_palindrome(nb):
        ans.append(" ".join((str(b), nb)))
if ans:
    print("\n".join(ans))
else:
    print("NIE")
