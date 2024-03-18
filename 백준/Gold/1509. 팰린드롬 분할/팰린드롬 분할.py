string = input()
n = len(string)
group = n
dp = [n for _ in range(n + 1)]
dp[-1] = 0
is_palindrome = [[0] * n for _ in range(n)]

for i in range(n):
    is_palindrome[i][i] = 1
    if i and string[i - 1] == string[i]:
        is_palindrome[i - 1][i] = 1

for i in range(2, n):
    for j in range(n - i):
        k = j + i
        if string[j] == string[k] and is_palindrome[j + 1][k - 1]:
            is_palindrome[j][k] = 1

for i in range(n):
    for j in range(i + 1):
        if is_palindrome[j][i]:
            dp[i] = min(dp[j - 1] + 1, dp[i])
        else:
            dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[-2])
