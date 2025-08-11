N = int(input())
*A, = map(int, input().split())
dp = [A[0]]
ans = 1

for i in range(1, N):
    a = A[i]

    if dp[-1] < a:
        dp.append(a)
        ans += 1
    else:
        for j in range(ans):
            if dp[j] >= a:
                dp[j] = a
                break

print(ans)